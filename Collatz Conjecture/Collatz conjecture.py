#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solution' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts LONG_INTEGER n as parameter.
#
def solution(n):
    '''
    This function generates the sequence for the Collatz Conjecture starting with a given integer n.
    
    Approach:
        1. Initialize an empty list `output` to store the sequence.
        2. Continue looping until n becomes 1:
            - Append the current value of n to the list `output`.
            - If n is even, update n to n // 2.
            - If n is odd, update n to 3 * n + 1.
        3. After the loop, append 1 to the `output` list.
        4. Return the sequence list.
    '''
    
    output = []
    while n != 1:
        output.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    output.append(1)  # Append 1 when n becomes 1
    
    return output

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    numberchange = solution(n)

    fptr.write(' '.join(map(str, numberchange)))
    fptr.write('\n')

    fptr.close()
