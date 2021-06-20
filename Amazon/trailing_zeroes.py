"""
Find the number of trailing zeroes in n!
"""

# method 1
# Result would be n/5 + n/25 + n/125 +.. until denom is smaller than n
# altering for loop iteration in this fashion is not supported by Python
#def countTrailingZeroesFac(n):
#    ans = 0
#    for i in range(5, n, 5*i):
#        ans += n/i

countTrailingZeroesFac(5)

# Method 2
# while n > 5
# ans += n/5

def countTrailingZeroesFac2(n):
    ans = 0
    while n >= 5:
        ans += n//5
        n /= 5
    return ans
countTrailingZeroesFac2(23)

### side quest

"""
Find the number of trailing zeroes in a given number n
"""

def countTralingZeroes(n):
    #120%10 = 0
    # 12%10 = 2

    # If the number has no trailing zeroes
    if n%10 :
        return 0

    count = 0
    while True:
        count += 1
        n = n/10
        if n%10:
            return count
        
print(countTralingZeroes(15000000))
        
    


