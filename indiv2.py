#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if not A:
        print("This list is empty.", file=sys.stderr)
        exit(1)

    a_max = A[0]
    i_max = 0
    for i, item in enumerate(A):
        if item > a_max:
            i_max, a_max = i, item

    print(f"The index of the maximum element: {i_max}")

    first_zero = -1
    for i, item in enumerate(A):
        if item == 0:
            first_zero = i
            break

    second_zero = -1
    if first_zero != -1:
        for i in range(first_zero + 1, len(A)):
            if A[i] == 0:
                second_zero = i
                break

    if first_zero == -1 or second_zero == -1:
        print("Not enough zeros")
    else:
        p = 1
        for i in range(first_zero + 1, second_zero):
            p *= A[i]
        print(f"The product between zero elements: {p}")

    odd = []
    even = []
    for i in range(len(A)):
        if i % 2 == 1:
            odd.append(A[i])
        else:
            even.append(A[i])

    odd.sort()
    even.sort()
    result = odd + even

    for x in result:
        print(x, end=' ')
    print()