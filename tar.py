#!/usr/bin/env python
#coding:utf-8

from __future__ import print_function
import os, re
import tarfile

__author__ = "bphanzhu@gmail.com"
__version__ = "0.1"

__tar_excludes__ =  ["\.svn$", "\.git$", ".*~$", ".*\.swp$"]

def __tar_filter__(tarinfo):
    realpath = os.path.realpath(tarinfo.name)
    for exclude in __tar_excludes__:
        if re.match(exclude, os.path.basename(tarinfo.name)):
            return None
    return tarinfo

def __tar_add__(archive, fname, verbose):
    if os.path.exists(fname):
        if __tar_filter__(tarfile.TarInfo(fname)):
            archive.add(fname, recursive=False)
            if verbose:
                print(fname)
            if os.path.isdir(fname):
                for name in os.listdir(fname):
                    __tar_add__(archive, os.path.join(fname, name), verbo)            
def tar_create(archive, fnames, compress="gz", verbose=True):
    if os.path.exists(archive):
        os.remove(archive)
    dstfile = tarfile.open(archive, mode="w|"+compress, format = tarfile.PAX_FORMAT)
    for fname in fnames:
        __tar_add__(dstfile, fname, verbose)
    dstfile.close()

def main(args):
    #TODO
    pass

if __name__ == "__main__":
    pass