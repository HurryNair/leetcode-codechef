"""
Write a one line function to return position of first 1 from right to left, in binary representation of an Integer. 
"""

import math

def getFirstSetBitPos(n):
    return int(math.log((n&-n), 2) + 1)

getFirstSetBitPos(12)