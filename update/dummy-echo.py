#! /usr/bin/python3

"""
update/dummy-echo.py

Stupidly echos updates.

Code from https://www.atlassian.com/git/tutorials/git-hooks/server-side-hooks
"""

import sys

branch = sys.argv[1]
old_commit = sys.argv[2]
new_commit = sys.argv[3]

print('update: Moving \'%s\' from %s to %s' % (branch, old_commit, new_commit))

