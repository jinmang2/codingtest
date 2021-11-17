#!/bin/python3

import math
import os
import random
import re
import sys

# problem link
# https://www.hackerrank.com/challenges/flipping-the-matrix

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    n = len(matrix[0]) // 2
    sum = 0
    for i in range(n):
        for j in range(n):
            upper_left = matrix[i][j]
            lower_left = matrix[i][2*n-1-j]
            upper_right = matrix[2*n-1-i][j]
            lower_right = matrix[2*n-1-i][2*n-1-j]
            sum += max(upper_left, max(lower_left, max(upper_right, lower_right)))
    return sum
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
