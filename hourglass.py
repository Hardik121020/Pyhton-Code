#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    list_1 =[]
    for i in range(len(arr)-2):
        for j in range(0,len(arr[i])-2):
            a = []
            d = []
            #print(array[i][j:j+3])
            d.append(arr[i][j:j+3])
            #print(array[i+1][j+1])
            a.append(arr[i+1][j+1])
            d.append(a)
            #print(array[i+2][j:j+3])
            d.append(arr[i+2][j:j+3])
            list_1.append(d)

    sum_list = []
    for i in list_1:
        total = 0
        for j in i:
            for k in j:
                total = total + k
        sum_list.append(total)
    return max(sum_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
