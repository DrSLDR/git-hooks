#! /usr/bin/python3

"""
pre-receive/dummy-echo.py

Stupidly echos incoming refs.

Code from https://www.atlassian.com/git/tutorials/git-hooks/server-side-hooks
"""

import fileinput

for line in fileinput.input():
    print('pre-receive: Trying to push ref %s' % line)
