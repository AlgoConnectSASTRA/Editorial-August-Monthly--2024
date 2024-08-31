#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solution' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER n
#  2. LONG_INTEGER_ARRAY heights
#
def solution(n, heights):
    '''
    Approach:
        1. Initialize `maximum` with the height of the first step to keep track of the highest step seen so far.
        2. Initialize `result` to 0, which will accumulate the total amount of "increased height" needed.
        3. Iterate through the heights list:
            - Update `maximum` to be the maximum of the current `maximum` and the current step height.
            - If the current step height is less than the `maximum`, add the difference (`maximum - heights[i]`) to `result`.
        4. Return the `result`, which represents the total height increases needed to make the heights non-decreasing.
    '''

    maximum = heights[0]
    result = 0

    for i in range(n):
        maximum = max(maximum, heights[i])
        if heights[i] < maximum:
            result += (maximum - heights[i])
    
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    heights = list(map(int, input().rstrip().split()))

    ans = solution(n, heights)

    fptr.write(str(ans) + '\n')

    fptr.close()
