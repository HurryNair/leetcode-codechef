"""
Highest power of 2 less than or equal to given number
"""

from math import log, pow

#Accept input integer
n = 500

print(pow(2,(int(log(n,2)))))

print("#"*40)

def highestpowerof2(n):
    
    for num in reversed(range(n)):
        if num & num-1 == 0:
            return num

print(highestpowerof2(500))
     
print("#"*40)



