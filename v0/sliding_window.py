"""
This technique shows how a nested for loop in some problems can be converted to a single for loop to reduce the time complexity.
"""

# Let’s start with a problem for illustration

"""
Given an array of integers of size ‘n’.
Our aim is to calculate the maximum sum of ‘k’ 
consecutive elements in the array.

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700
"""

# O(n^2) solution

def maxSumofK(array, n, k):

    res = float('-inf')

    for i in range(n-k+1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + array[i + j]
        
        res = max(res, current_sum)
    
    return res

if __name__ == '__main__':
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    n = len(arr)
    print(maxSumofK(arr, n, k))

# Window Sliding Technique

def maxSumofK(array, k, n):

    if n < k:
        print("Invalid input")
        return -1

    window_sum = sum(array[:k])

    max_sum = window_sum

    for i in range(n-k):
        window_sum = window_sum - array[i] + array[i+k] # window sliding
        max_sum = max(window_sum, window_sum)
    
    return max_sum

if __name__ == '__main__':
    array = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    print(maxSumofK(arr, k, len(array)))


