"""
Permutation of n numbers with no adjacent numbers whose difference is 1

Given n compute such beautiful permutation if it exits.
"""

def computeBeautifulPerm(n):

    # edge cases
    if n == 1:
        print(1)
        return 0
    
    elif (n ==2 or n ==3):
        print("No Solution")
        return 0

    # For 4 we only see one perm - 2 4 1 3

    if n%2 == 0:
        for i in range(2, n+1, 2): # Directly print to out from here
            print(i, end = " ")
        for j in range(1, n, 2):
            print(j, end = " ")
    else:
        for i in reversed(range(2, n, 2)):
            print(i, end = " ")
        for j in reversed(range(1, n+1, 2)):
            print(i, end = " ")

if __name__ == "__main__":
    computeBeautifulPerm(4)



