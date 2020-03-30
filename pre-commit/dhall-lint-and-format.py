#!/usr/bin/python3 

import os
import subprocess
import re

passed = True

dhall_pattern = re.compile(r'.*\.dhall$')

dhall_files = []
temt_files = []
maxlen = 0

def dhall_check(keyword, dhall_file):
    done_process = subprocess.run(['dhall', keyword, '--check',
                                    '--inplace', dhall_file],
                                    stdout=subprocess.DEVNULL,
                                    stderr=subprocess.DEVNULL)
    return done_process.returncode


def dhall_format(dhall_file):
    return dhall_check('format', dhall_file)


def dhall_lint(dhall_file):
    return dhall_check('lint', dhall_file)

done_process = subprocess.run(
    ['git', 'status', '--porcelain'],
    stdout=subprocess.PIPE)
status = done_process.stdout.decode('utf-8')
for line in status.split('\n'):
    line_length = len(line)
    if (line_length > 0 and 
        (line[0] == 'M' or line[0] == "A") and 
        dhall_pattern.match(line)):
        dhall_files.append(line[3:])
        if line_length > maxlen:
            maxlen = line_length - 3

for dhall_file in dhall_files:
    diff = maxlen - len(dhall_file)
    printstr = "Checking " + dhall_file + '...' + ' '*(diff + 2)
    errlist = []
    done_process = subprocess.run(
        ['git', 'checkout-index', '--temp', dhall_file],
        stdout=subprocess.PIPE
    )
    alias = done_process.stdout.decode('utf-8')
    dhall_file = alias.split('\t')[0]
    temt_files.append(dhall_file)
    if dhall_format(dhall_file) != 0:
        errlist.append("FORMAT")
    if dhall_lint(dhall_file) != 0:
        errlist.append("LINTER")
    
    if len(errlist) == 0:
        printstr += "OK"
    else:
        printstr += "ERROR " + " ".join(errlist)
        passed = False
    print(printstr)

for temp_file in temt_files:
    os.remove(temp_file)

if not passed:
    print("Commit refused by pre-commit hook. Dhall files unformatted.")
    os.sys.exit(1)