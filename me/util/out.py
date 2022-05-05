#!/usr/bin/env python
# -*- coding:utf-8 -*-

def pprint(o):
    import pprint
    pp = pprint.PrettyPrinter(indent=2)
    if o is not None:
        pp.pprint(o)
