"""
Given two strings, the task is to find if a string can be obtained by rotating another string two places.
"""

# String slicing is the way to rotate a string in python

# utility function to rotate string clockwise two places (right shift)

def rotateClockwise(s):
    s_rotated = s[-2:] + s[:-2] # last two chars + rest of string
    return s_rotated

# utility function to rotate string anti-clockwise two places (left shift)
def rotateAntiClockwise(s):
    s_rotated = s[2:] + s[:2] # last two chars + rest of string
    return s_rotated

def isRotated(str1, str2):
    if (len(str1) != len(str2)):
        return False
    
    if (len(str1)<2):
        return str1 == str2
    
    rot1 = rotateClockwise(str1)
    rot2 = rotateAntiClockwise(str1)

    return (rot1 == str2 or rot2 == str2)

if __name__ == "__main__":

    str1 = "geeks"
    str2 = "eksge"

    if isRotated(str1, str2):
        print("Yes")
    
    else:
        print("No")




