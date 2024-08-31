#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER N as parameter.
#

def solution(N):
    '''
    This function calculates the minimum number of swaps required based on the given integer N.
    
    The approach:
    1. If N is even, each pair of elements can be swapped with a single swap operation.
    2. If N is odd, one additional swap is needed beyond the pairs.
    3. The result is computed as the integer division of N by 2 plus the remainder when N is divided by 2.
    
    This simplifies to: (N % 2) + (N // 2)
    - (N % 2) accounts for the extra swap needed if N is odd.
    - (N // 2) accounts for the pairs of elements that can be swapped.
    '''
    return (N % 2) + (N // 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        N = int(input().strip())

        a = solution(N)

        fptr.write(str(a) + '\n')

    fptr.close()
