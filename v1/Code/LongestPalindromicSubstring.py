# Brute Force
# Generate all possible substrings in O(n^2) time
# Check if each substring is a palin - another O(n)
# O(n^3) solution

def ifPalindrome(s):
    l = 0
    r = len(s)-1

    while(l<r):
        if(s[l] != s[r]):
            return False
        else:
            l += 1
            r -= 1
    
    return True

def longestPalindrome(s):
    n = len(s)
    maxSoFar = 0

    for i in range(0, n):
        for j in range(i+1,n):
            if ifPalindrome(s[i:j+1]):
                if (j-i+1) > maxSoFar:
                    maxSoFar = j-1+1
    return maxSoFar

# Optimized approach

def longestPalindrome2(s):

    res_l = 0
    res_r = 0
    resLen = 0

    n = len(s)
    for i in range(n):
        l,r = i, i
        while(l >= 0 and r < n and s[l] == s[r]):
            if (r-l+1) > resLen:
                resLen = r-l+1
                res_l = l
                res_r = r
            l -= 1
            r += 1

        l = i
        r = i+1
        while(l >= 0 and r < n and s[l] == s[r]):
            if (r-l+1) > resLen:
                resLen = r-l+1
                res_l = l
                res_r = r
            l -= 1
            r += 1
    
    return s[res_l:res_r+1]

if __name__ == "__main__":
    s = "babad"
    print(longestPalindrome2(s))
    s = "cbbd"
    print(longestPalindrome2(s))


