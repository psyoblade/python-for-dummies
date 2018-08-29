#!/usr/bin/env python
# -*- coding:utf-8 -*-
from types import *

def print_sequence(seq):
    print(sorted(seq))

# output_expression = [ variable in input_sequence if_conditions ]
def square_using_comprehension(ints):
    return [ x**2 for x in ints if type(x) == int ]

def square_using_lambda_and_filter(ints):
    return list(map(lambda x: x**2, filter(lambda x: type(x) == int, ints)))

ints = [ 1, '2', 3, 'a', 5, 0 ]
a = print_sequence(square_using_comprehension(ints))
b = print_sequence(square_using_lambda_and_filter(ints))
assert(a == b)