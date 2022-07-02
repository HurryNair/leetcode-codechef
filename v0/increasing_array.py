"""
Given an array turn it into ascending.

Each turn you may increase val of one element by one. How many turns do you need ?
"""

def arrayToAscending(n, l, ans = 0, mx = 0):
    for num in l:
        mx = max(mx, num) # Greatest number found so far
        ans += mx - num
    
    return ans

if __name__ == "__main__":
    n = 5
    l = [3, 2, 5, 1, 7]

    print(arrayToAscending(n, l))



    
