def equilibriumPoint(A, N):
    # Your code here
    if N == 1:
        return 1
    
    elif N == 2:
        return -1
    
    else:
        
        sum = [0*i for i in range(N)]
        
        for i in range(N):
            if i == 0:
                sum[i] = A[i]
            else:
                sum[i] = sum[i-1] + A[i]
        
        print(sum)
        array_sum = sum[-1]
        
        for i in range(N):
            l_sum = sum[i] - A[i]
            r_sum = array_sum - sum[i]
            
            if l_sum == r_sum:
                return i

        else:
            return -1



#{ 
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = 1

    while(T > 0):

        N = 5

        A = [1,3,5,2,2]

        print(equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()
