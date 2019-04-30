# !/usr/bin/env python3
# -*- coding: utf8 -*-
# PCL II
# Assignment 04
# Exercise 02
# Olivier Fischer

from typing import Iterable

def longest_substrings(x: str, y: str) -> Iterable[str]:
    '''returns list of longest substrings of two given strings'''
    x, y = x.lower(), y.lower()
    longest, indices = 0, []
    n, m = len(x), len(y)
    d = [[None for _ in range(m+1)] for _ in range(n+1)]
    d[0][0] = 0
    for i in range(1, n+1):
        d[i][0] = 0
    for j in range(1, m+1):
        d[0][j] = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                v = d[i-1][j-1] + 1
                d[i][j] = v
                if v < longest:
                    continue
                elif v > longest:
                    indices = []
                    longest = v
                indices.append(i-1)
            else:
                d[i][j] = 0
    # for i in range(n+1):
	    # print(' ' + ' '.join(map(str, d[i])) + ' ')
    if indices == []: return None
    else: return [x[i+1-longest:i+1] for i in indices]
    
def main():    
    print(longest_substrings('meisterklasse', 'kleistermasse'))
    print(longest_substrings('Tod', 'Leben'))
    print(longest_substrings('Haus', 'Maus'))
    print(longest_substrings('mozart','mozzarella'))
    print(longest_substrings('keep the interface!', 'KeEp ThE iNtErFaCe!'))

if __name__ == "__main__":
    main()