#!/usr/bin/env python

import unittest
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import shell_util

class ShellUtilTest(unittest.TestCase):

    def setUp(self):
        #TODO
        pass

    def test_cd(self):
        pass

    def test_tar_create(self):
        pass

if __name__ == "__main__":
    unittest.main()
