"""
You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.
"""

# Bitmask dynamic programming/memorization

# We plan to form a powerset

# [1,2,3,4,5,6]
# Powerset for above set would be
# [1], [2], [3], [1,2]

