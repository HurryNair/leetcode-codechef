class Solution:
    
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n-1):
            nb = decimalToBinary(n, i)
            if not isPalin(nb):
                return False
        return True

def decimalToBinary(n, b):
    if n >= 1:
        return decimalToBinary(n//b, b) + str(n%b)
    else:
        return ''
        
def isPalin(nb):
    if nb == nb[::-1]:
        return True
    else:
        return False