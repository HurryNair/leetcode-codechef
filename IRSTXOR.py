# Filename : IRSTXOR.py
#! /bin/usr/python3

'''
You are given an integer C. Let d be the smallest integer such that 2d is strictly greater than C.

Consider all pairs of non-negative integers (A,B) such that A,B<2d and A⊕B=C (⊕ denotes the bitwise XOR operation).

Find the maximum value of A⋅B over all these pairs.

Example Input
2
13
10

Example Output
70
91

Explanation
Example case 1: The binary representation of 13 is "1101". 
We can use A=10 ("1010" in binary) and B=7 ("0111" in binary). 
This gives us the product 70. No other valid pair (A,B) can give us a larger product.

Example case 2: The binary representation of 10 is "1010". 
We can use A=13 ("1101") and B=7 ("0111"). This gives us the maximum product 91.

'''