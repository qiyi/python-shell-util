#!/usr/bin/env python
#coding:utf-8

from __future__ import print_function
import os

__author__ = "bphanzhu@gmail.com"
__version__ = "0.1"

def cd(dir):
    '''
    chdir to target place
    dir: the target realpath
    '''
    os.chdir(os.path.realpath(dir))
    print("chdir:"+os.getcwd())

if __name__ == "__main__":
    pass
    
