#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Given an array of five positive integers
# return two integers representing the max and min variables
# arr = [1,3,5,7,9] ---> min sum = 1+3+5+7, max sum = 3+5+7+9 returns 16 24
# sort the list ascending, extract first 4, last 4, sum the 4, return the two sums


def miniMaxSum(arr):
    min_sum, max_sum = 0,0
    arr = sorted(arr)
    
    for num in arr[:4]:
        min_sum += num;
        
    for num in arr[1:]:
        max_sum += num
        
    print(f'{min_sum} {max_sum}')

    
def add(arr):
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
