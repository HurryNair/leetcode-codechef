"""
Given a number n, verify if its possible to divide the numbers 1,2,3...n into two sets of equal sum
Print "YES" or "NO"
If "YES" print the number of elements as well as the elements in each set

https://www.youtube.com/watch?v=dZ_6MS14Mg4
https://www.youtube.com/watch?v=QGVCnjXmrNg

N = 11
Sum = 132

1 2 3 4 5 6 7 8 9 10 11

1 2 3 4 ==> 1 4 || 2 3

1 2 3 4 5 6 7 8 ==> 1 4 5 8 || 2 3 6 7

1 2 3 4 5 6 7 8 9 10 11 12 ==> 1 4 5 8 9 12 || 2 3 6 7 10 11

// Look at the input in windows of 4
// 


"""

def two_sets(n):

    if (n*(n+1)/2)%2 : # If n-sum is odd
        print("NO") # No way we can split it into 2 equal sets
        return 0

    l1 = []
    l2 = [] # data containers to hold the two equal sets

    # Find the number of 4 sized windows we can have 
    # Add elements 1 & 4 from each of these windows to one list & 
    # elements 2 & 3 to the other
    if n%4 : # if n is odd, offset by 3 so that the last 3 items are calculated 
        j = 3
    else: # if n is odd, offset by 4 so that the last 4 items are calculated 
        j = 4
    for i in range(0, int((n-1)/4)):
        l1.append(4*i+1+j)
        l1.append(4*i+4+j)
        l2.append(4*i+2+j)
        l2.append(4*i+3+j)

    # For the portion of the array [1,2..n] after the last 4 sized window

    if (n%4): # last portion would have 3 items
        l1.append(1)
        l1.append(2)
        l2.append(3)
    else:
        l1.append(1)
        l1.append(4)
        l2.append(3)
        l2.append(2) 
    
    # For the last portion of the array, we cant be sure what times of original value to add
    # We therefore go back & offset first list by 3 or 4 based on n%4 so that the last values
    # are calculated there & add the first ones here directly above the comment

    print("YES")

    n = len(l1)
    print(n)
    for num in l1:
        print(num, end = " ")
    
    print("")

    n = len(l2)
    print(n)
    for num in l2:
        print(num, end = " ")

if __name__ == "__main__":
    two_sets(3)

    









