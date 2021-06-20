"""
Given a string your task is to reorder its letters in such a way that it becomes a palindrome
"""

# Approach 1
# Count characters & store them into a dictionary
# If the number of odd elements in dict.values() > 1: return "No"

def make_palin_d(s):

    # dictionary to count occurences
    d = {}

    # Logic to count occurences
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    
    # Grab just the values
    d_vals = d.values()

    # Counter c to keep track of number of chars supplied odd times
    c = 0
    for num in d_vals:
        if num%2:
            c += 1
    
    if c > 1:
        print("No Solution")
        return 0
    
    # By this point we're sure a palin can be formed with the supplied chars

    palin = "" # result
    odd_char = ""

    for char in d:
        if d[char]%2==0:
            for i in range(int(d[char]/2)):
                palin += char
        else:
            odd_char += char
    
    mid = ""
    for i in range(d[odd_char]):
        mid += odd_char
    
    print(palin+mid+palin[::-1])
    
make_palin_d("AAAACACBA")

# Approach 2
# Create an array of integers
# Iterate through the string
# Mark alphabets that are present in the array; list[ord[c] - ord['A']] += 1
# Counter c to keep track of number of chars supplied odd times
# Odd number & 1 = 1; If yes increment c; Even number & 1 = 0;
# If c > 1: return "No"

def make_palin(s):
    alphabets = [0]*26 # list with its values repesenting the number of occurences of char(index)

    # Logic to count the number of occurences of each alphabet
    for char in s:
        alphabets[ord(char)-ord('A')] += 1

    # Logic to ensure no more than one char has been supplied odd number of times
    c = 0
    for i in range(26):
        c += alphabets[i]&1 # expression returns 1 only when c[i] is odd
    if c>1:
        print("No")
        return 0
    
    # By this point we're sure a palin can be formed with the supplied chars

    palin = "" # result

    for i in range(26):
        if (alphabets[i]&1^1): # expression evaluates to 1 only when alphabets[i] is even
            for j in range(0, int(alphabets[i]/2)): # Get half of whatever the supplied char is
                palin += chr(ord('A')+i) # Convert index back to char & append to result
    
    # Half the string is completed
    # Logic to handle chars supplied odd times

    mid = ""
    for i in range(26):
        if (alphabets[i]&1): # pick just the one char with odd supplies
            for j in range(alphabets[i]): # present them all in the middle
                mid += chr(ord('A')+i)
    
    print(palin+mid+palin[::-1])

make_palin("AAAACACBA")


    


        










    


