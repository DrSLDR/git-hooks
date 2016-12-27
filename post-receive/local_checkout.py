#! /usr/bin/python3

"""
post-receive/local-merge.py

Merges the just-pushed update into another working tree.
"""

import os
import subprocess
import sys

# Configs
LOCALDIR = os.path.abspath('/path/to/.git')
BRANCH = 'master'
REMOTE = 'origin'

# Set working directory (redundantly)
os.chdir(LOCALDIR)
os.environ['GIT_WORK_TREE'] = os.path.dirname(LOCALDIR)

# Fetch relevant data
COMMAND = ['git', 'fetch', REMOTE, BRANCH]
OUT = subprocess.call(COMMAND, cwd=LOCALDIR, stderr=subprocess.DEVNULL)
if not OUT == 0:
    print('post-receive: FATAL: could not fetch (%s)' % OUT)
    sys.exit(1)

# Merge into local
COMMAND = ['git', 'checkout', '-f', REMOTE + '/' + BRANCH]
OUT = subprocess.call(COMMAND, cwd=LOCALDIR, stderr=subprocess.DEVNULL)
if not OUT == 0:
    print('post-receive: FATAL: could not check out (%s)' % OUT)
    sys.exit(2)

# Report back
print('post-receive: Merged with update in %s' % LOCALDIR)
