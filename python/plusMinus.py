#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# an array of positive, negation, and zero numbers
# print line ratio of pos, neg, zero numbers
# arr = [-4,3,-9,0,4,1] --> .5, .33333, .166667
#f'{ratio.6f}'



def plusMinus(arr):
    ratio_arr = [0, 0, 0]
    fill = 6
    
    for num in arr:
        if num > 0:
            ratio_arr[0] += 1
        elif num < 0:
            ratio_arr[1] += 1
        else:
            ratio_arr[2] += 1
            
    for ratio in ratio_arr:
        if ratio == 0:
            print(f'{ratio:.6f}')
        else:
            print(f'{(ratio/len(arr)):.6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
