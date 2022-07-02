# Filename : IRSTXOR.py
#! /bin/usr/python3

'''
You are given an integer C. Let d be the smallest integer such that 2**d is strictly greater than C.

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

# Accept inputs
t = int(input())

for i in range(t):
    C = int(input())

    # define d by implementing log
    import math
    d = int(math.log(C, 2)) + 1

    # brute force solution
    max_prod = 0
    for i in range(0, 2**d):
        print("i" + str(i))
        for j in range(i+1, (2**d)+1):
            print("j" + str(j))
            print(i^j)
            if i^j == C:
                if i*j > max_prod:
                    max_prod = i*j
    
print(max_prod)

    # bit manipulation techniques
    # Find number of bits in C, call this bit_count
    # Let A be 2**(bit_count-1)-1; Found this pattern on both test inputs
    # Since what we need is A ^ B = C
    # A ^ A ^ B = A ^ C
    # B = A ^ C
    # Compute A*B & return it

    temp = C

    bit_count = 0
    while C > 0:
        temp = temp/2
        bit_count += 1
    
    # Define A
    A = 2**(bit_count-1) - 1
    # Find B
    B = A ^ C

    print(A*B)



