#!/usr/bin/env python
TODO_2018_08_28 = """
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
https://docs.python.org/3.6/library/timeit.html
https://docs.python.org/3.6/library/debug.html
https://docs.python.org/3.6/library/collections.html
"""

def generate():
    M = [[1,2,3],[4,5,6],[7,8,9]]
    G = (sum(row) for row in M)
    return G

def main():
    G = generate()
    print(next(G))
    print(next(G))
    print(next(G))

if __name__ == "__main__":
    main()