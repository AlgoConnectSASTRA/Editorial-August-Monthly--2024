#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solution' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. LONG_INTEGER a
#  2. LONG_INTEGER b
#

def solution(a, b):
    '''
        The function determines if it's possible to make both heaps empty by performing the following operations:
        - Remove 2 from heap A and 1 from heap B
        - Or remove 1 from heap A and 2 from heap B

        Approach:
        1. Continue to perform operations based on the larger heap:
           - If heap A is larger, remove 2 from A and 1 from B.
           - If heap B is larger or equal, remove 2 from B and 1 from A.
        2. Stop when at least one heap is empty.
        3. If both heaps are empty, return "YES"; otherwise, return "NO".

        
    '''
    
    while a>0 or b>0:
        if a>b:
            a-=2 
            b-=1
        else:
            b-=2
            a-=1
    return 'YES' if (a==0 and b==0) else 'NO'
        
    
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        ans = solution(a, b)

        fptr.write(ans + '\n')

    fptr.close()
