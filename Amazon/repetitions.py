"""
Given a DNA sequence with A, C, G & T find the longest substring with identical characters
"""

def longestSubstr(s):
    ans = 1 # Longest possible substr is by default 1
    c = 0 # counter
    l = "A" # set l to arbitrary char from string
    for char in s:
        if char == l: # identical char found
            c += 1
            ans = max(ans, c)
        
        else: # Different char found
            l = char
            c = 1 # First occurence
        
    return ans

if __name__ == "__main__":
    print(longestSubstr("ACCCGT"))
