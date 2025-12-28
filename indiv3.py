#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = tuple(map(int, input().split()))

    if not A:
        print("This list is empty.", file=sys.stderr)
        exit(1)

    for i in range(len(A) - 1):
        if A[i] % 2 == 1 and A[i + 1] % 2 == 1:
            print(f"Indexes of adjacent odd numbers: {i, i + 1}")
            break
    else:
        print("There are no adjacent odd numbers")