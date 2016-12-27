#! /usr/bin/python3

"""
post-receive/local-merge.py

Merges the just-pushed update into another working tree.
"""

import os
import subprocess
import sys

# Configs
LOCALDIR = os.path.abspath('/path/to/git/repo')
BRANCH = 'master'
REMOTE = 'origin'

# Set working directory (redundantly)
os.chdir(LOCALDIR)

# Fetch relevant data
if not subprocess.call(['git', 'fetch', REMOTE, BRANCH], cwd=LOCALDIR,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL):
    print('post-receive: FATAL: could not fetch')
    sys.exit(1)

# Merge into local
if not subprocess.call(['git', 'checkout', '-f', REMOTE + '/' + BRANCH],
                       cwd=LOCALDIR, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL):
    print('post-receive: FATAL: could not merge')
    sys.exit(2)

# Report back
print('post-receive: Merged with update in %s' % LOCALDIR)
