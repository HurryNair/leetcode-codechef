"""
Chef has N 6-sided standard dice. Each die has dimensions 1×1×1. Since Chef is bored during the quarantine, he decides to stack dice for fun.

First, Chef forms four vertical stacks of dice (not necessarily with the same height; empty stacks are allowed) on his table, which together make up a pile of dice with base area up to 2×2. Among all such structures, the total visible surface area of Chef's structure must be the smallest possible.

Then, Chef calculates the number of pips on the visible faces of all dice in the structure. A face of a die is visible if it does not touch the table or another die.

Now, he is wondering: among all possible arrangements of dice, what is the maximum possible total number of visible pips? Since he is busy cooking, he is asking you to solve this.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains a single integer N.
Output
For each test case, print a single line containing one integer ― the maximum possible number of visible pips.

Constraints
1≤T≤105
1≤N≤1012
Subtasks
Subtask #1 (10 points):

T≤100
N≤4
Subtask #2 (10 points):

T≤100
N≤8
Subtask #3 (25 points):

T≤100
N≤104
Subtask #4 (55 points): original constraints

Example Input
1
1
Example Output
20
"""

# cook your dish here

# Test cases
# 1 die - 5 visible faces - max pips = 20
# 2 dice - stacked sideways - 4 visible faces on each die - max pips = 18 + 18 = 36
# 3 dice - 3 visible faces one one die & 4 visible faces on 2 dice - max pips = 15 + 18 + 18 = 51
# 4 dice - 3 visible faces per die - 15 + 15 + 15 + 15 = 60

# 5 dice - 
# bottom layer - 2 visible faces on one die & 3 visible faces on 3 dice - max pips = 11 + 45 = 56
# top layer - Same as - 1 die - 5 visible faces - max pips = 20
# total pips = 76

# 6 dice -
# bottom layer - 2 visible faces on two dice & 3 visible faces on 2 dice - max pips = 11 + 11 + 15 + 15 = 52
# top layer - Same as - # 2 dice - stacked sideways - 4 visible faces on each die - max pips = 18 + 18 = 36
# total pips = 88

# 7 dice -
# bottom layer - 2 visible faces on three dice & 3 visible faces on 1 dice - max pips = 11 + 11 + 11 + 15 = 48
# top layer - Same as - 3 dice - 3 visible faces one one die & 4 visible faces on 2 dice - max pips = 15 + 18 + 18 = 51
# total pips = 99

# 8 dice -
# bottom layer - 2 visible faces on four dice - max pips = 11 + 11 + 11 + 11 = 44
# top layer - Same as - 4 dice - 3 visible faces per die - 15 + 15 + 15 + 15 = 60
# total pips = 104

# Accept input for the number of test cases
t = int(input())

# In this dictionary we store values of max pips for a given set of dies
max_pips_die = {0:0, 1:20, 2:36, 3:51, 4:60}

for i in range(t):
    
    # Accept n from input
    n = int(input())
    
    if n <= 4:
        print(max_pips_die[n])
    elif n > 4:
        # If n>4 then we are no more on layer 1
        
        q = n//4 # quotient # Indicates the layers beneath the one we are working on
        r = n%4 # reminder # Indicates the number of dice in the current layer
        
        #print("pips on layers_under_me : ", q*max_pips_die[4])
        #print("pips on me : ", max_pips_die[r])
        print((q*max_pips_die[4] + max_pips_die[r]) - (n-4)*4)
