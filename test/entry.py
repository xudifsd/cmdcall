#!/usr/bin/env python

from __future__ import print_function

import sys

sys.path.insert(0, "../src")

import cmdcall

def foo(a, b, c="1", d=None):
    print("in foo, a = {}, b = {}, c = {}, d = {}".format(a, b, c, d))
    return int(a) + int(b) + int(c) + (int(d) if d is not None else 0)

if __name__ == '__main__':
    sys.exit(cmdcall.handle(sys.modules[__name__]))
