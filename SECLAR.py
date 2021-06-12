"""
Given three distinct integers A, B and C, print the second largest number among them.

Input:
The input consists of three lines.
The first line contains a single integer A.
The second line contains a single integer B.
The third line contains a single integer C.
Output:
Print the second largest number among A, B and C, in a separate line.

Constraints
1≤A,B,C≤109
Sample Input 1:
2
7
21
Sample Output 1:
7
Sample Input 2:
14
28
16
Sample Output 2:
16
EXPLANATION:
In the first example, 7 is the second largest number among the given three numbers.
In the second example, 16 is the second largest number among the given three numbers.
"""

# cook your dish here

largest = second = float('-inf')

l = []

for i in range(3):
    l.append(int(input()))
    
# Inputs are now stored in array l

# We traverse the array twice
# First time we find max
# second time we look for largest number less that max

for i in range(3):
    if l[i] > largest:
        largest = l[i]

for i in range(3):
    if l[i] != largest:
        if l[i] > second:
            second = l[i]

print(second)