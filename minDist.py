import sys
def minDist(arr, n, x, y):
    # Code here
    
    m = sys.maxint
    flag = 0
    
    for i in range(0, n-1):
        if arr[i] == x or arr[i] == y:
            for j in range(i+1, n):
                if arr[j] == x or arr[j] == y:
                    if arr[j] != arr[i]:
                        flag = 1
                        print(i, j)
                        m = min(m, j - i)
    if flag == 0:
        return -1
    else:
        return m
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = 1
    for i in range(t):
        n = 95
        arr = [94, 36, 35, 59, 48, 12, 50, 86, 43, 95, 4, 5, 36, 28, 61, 82, 75, 13, 54, 58, 24, 9, 59, 88, 64, 74, 80, 18, 42, 41, 64, 87, 76, 99, 45, 75, 10, 46, 61, 4, 92, 16, 60, 28, 96, 20, 61, 70, 84, 14, 79, 8, 75, 37, 47, 90, 10, 26, 8, 3, 18, 71, 89, 94, 21, 85, 20, 82, 82, 32, 86, 73, 48, 45, 52, 43, 17, 64, 12, 100, 78, 42, 59, 52, 30, 6, 41, 91, 83, 100, 93, 1, 23, 33, 94]
        x,y = 42,68
        print(minDist(arr, n, x, y))



# } Driver Code Ends
