def majorityElement(A,N):
    #Your code here
    d = {}
    
    for i in range(N):
        if A[i] not in d:
            d[A[i]] = 1
            if d[A[i]] > N/2:
                return A[i]
        else :
            d[A[i]] += 1
            if d[A[i]] > N/2:
                return A[i]
    return -1
