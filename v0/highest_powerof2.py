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

# Application problems

"""
Some people are standing in a queue. A selection process follows a rule where people standing on even positions are selected. 
Of the selected people a queue is formed and again out of these only people on even position are selected. 
This continues until we are left with one person. Find out the position of that person in the original queue. 
Print the position(original queue) of that person who is left. 
"""








