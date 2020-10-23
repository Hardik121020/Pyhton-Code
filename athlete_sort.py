#!/bin/python3

import math
import os
import random
import re
import sys

def athlete_sort(k1,arr1):
    rows = sorted(arr1, key = lambda x: x[k1])
    for i in rows:
        for j in i:
            print(j, end=" ")
        print()

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    athlete_sort(k,arr)
