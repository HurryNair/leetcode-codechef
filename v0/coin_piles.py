"""
You have two coin piles containing a and b coins.
On each move you can either move one coin from the left pile and two from the right
Or viceversa. Find out if you can efficiently empty both piles.
"""

# Analysis
# If a or b is 1 or 2, I cannot efficiently empty
# If a and b is 3 and 3, we can efficiently empty

# Thought process
# Every time we remove 3 coins
# So if this was a single pile, we would need count%3 = 0

def empty_piles(a, b):
    if (a+b)%3==0 and 2*a >= b and 2*b >= a:
        print("Yes")
    else:
        print("No")