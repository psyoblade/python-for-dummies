#!/usr/bin/env python
# -*- coding:utf-8 -*-

identity_matrix = [
    [1,0,0],
    [0,1,0],
    [0,0,1]]

# [ [ output if_condition inner_iteration ] outer_iteration ]
def identity_matrix_using_double_for(size):
    return [[ 1 if inner == outer else 0 for inner in range(0, size)] for outer in range(0, size)]

a = identity_matrix
b = identity_matrix_using_double_for(3)
assert(a == b)