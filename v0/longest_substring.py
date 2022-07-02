"""
Given a string str, find the length of the longest substring without repeating characters. 

For “ABDEFGABEF”, the longest substring are “BDEFGA” and “DEFGAB”, with length 6.
For “BBBB” the longest substring is “B”, with length 1.
For “GEEKSFORGEEKS”, there are two longest substrings shown in the below diagrams, with length 7
"""

# utility function to check if a given string is unique
def isUnique(s, i, j):

    visited = [0] * 26 # Map to track visited alphabets

    for k in range(i, j+1):
        
        if visited[ord(s[k])-ord('a')] == True: # If character is already marked visited
            return False

        visited[ord(s[k])-ord('a')] = True # Mark character as visited in the map
    
    return True # return True if control reaches this point

# Function to find the largest unique substring
def largestUniqSubstr(s):

    n = len(s)

    res = 0 # var to keep track of largest substr found so far

    for i in range(n):
        for j in range(i, n): # These two lines spawn n*(n+1)/2 substrings. Each of these require to be looked at with O(n) complexity
            if isUnique(s, i, j):
                res = max(res, j-i+1)

    return res

if __name__ == '__main__':

    s = "geeksforgeeks"

    print("Input substring: ", s)

    print("Length of longest unique substring: ", largestUniqSubstr(s))

"""
Method 2 (Better : O(n2)) The idea is to use window sliding. Whenever we see repitition, we remove the pervious occurrance and slide the window.
"""

def longestUniqueSubsttr(str):
     
    n = len(str)
     
    # Result
    res = 0
  
    for i in range(n):
          
        # Note : Default values in
        # visited are false
        visited = [0] * 256  
  
        for j in range(i, n):
  
            # If current character is visited
            # Break the loop
            if (visited[ord(str[j])] == True):
                break
  
            # Else update the result if
            # this window is larger, and mark
            # current character as visited.
            else:
                res = max(res, j - i + 1)
                visited[ord(str[j])] = True
             
        # Remove the first character of previous
        # window
        visited[ord(str[i])] = False
     
    return res
 
# Driver code
str = "geeksforgeeks"
print("The input is ", str)
 
len = longestUniqueSubsttr(str)
print("The length of the longest "
      "non-repeating character substring is ", len)
 
###### This code is contributed by sanjoy_62

"""
Method 3

Using a stack
"""

def largestUniqueSubstr(string):

    stack = [] # A stack to keep track of the current substring
    max_len = 0 # result
            
    if len(string) == 1:
        return 1
            
    if len(string) > 1:
        for char in string: # Traverse through the string
            if char not in stack: # If currect char is not in stack
                stack.append(char) # Push it onto the stack
                max_len = max(max_len, len(stack)) # calculate new max
            elif char in stack:
                print(char)
                print(stack)
                stack = stack[stack.index(char)+1:]
                print(stack)
                stack.append(char)
    
    return max_len

print(largestUniqueSubstr("geeksforgeeks"))

                




    






