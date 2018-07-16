#!/usr/bin/env python

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