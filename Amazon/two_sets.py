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

    if (n*(n+1)/2)%2 : # If the n-sum is negative, we have no ways to split it equally
        print("NO")







