import sys
def minDist(arr, n, x, y):
    # Code here
    
    p = -1
    m = sys.maxsize
    
    for i in range(n):
        
        if arr[i] == x or arr[i] == y:
            
            if p != -1 and arr[p] != arr[i]:
                m = min(m, i-p)
            
            p = i
    
    if m == sys.maxsize:
        return -1
    else:
        return m
