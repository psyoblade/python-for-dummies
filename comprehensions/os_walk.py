#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

# [ value ]
def os_walk_dirs(root, ext):
    return [os.path.join(d[0], f) for d in os.walk(root) for f in d[2] if f.endswith(ext)]

# for python_file in os_walk_dirs('.', '.py'):
#     print(python_file)

inner_outer = [str(inner) + ":" + str(outer) for inner in range(0,5) for outer in range(6,9)]
print(inner_outer)

outer_inner = [[str(inner) + ":" + str(outer) for inner in range(0,5)] for outer in range(6,9)]
print(outer_inner)

assert(inner_outer != outer_inner)