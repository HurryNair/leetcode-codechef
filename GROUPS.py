# Filename : GROUPS.py
#! /usr/bin/python3

'''
There are N seats in a row. 
You are given a string S with length N; for each valid i, 
the i-th character of S is '0' if the i-th seat is empty or '1' if there is someone sitting in that seat.

Two people are friends if they are sitting next to each other. Two friends are always part of the same group of friends. 
Can you find the total number of groups?

Example Input
4

000
010
101
01011011011110

Example Output

0
1
2
4
'''

t = int(input())
for i in range(t):
    # Accept input string
    s = input()
    
    # Implement a flag to keep track of 0 => 1 transitions 
    # & vice-versa

    flag = 0
    count = 0
    
    for num in s:
        # logic to detect 0 => 1 transitions
        if num == '1':
            if flag == 0:
                count += 1
                flag = 1
        
        # logic to detect 1 => 0 transitions
        elif num == '0':
            if flag == 1:
                flag = 0
        
    print(count)


