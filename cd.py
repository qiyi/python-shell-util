#!/usr/bin/env python
#coding:utf-8

import os

__author__ = "bphanzhu@gmail.com"
__version__ = "0.1"

def cd(dst):
    '''
    chdir to target place
    dst: the target realpath
    '''
    os.chdir(os.path.realpath(dst))

if __name__ == "__main__":
    import tempfile
    dst = tempfile.gettempdir()
    cd(dst)
    assertEquals(dst, os.getcwd())
