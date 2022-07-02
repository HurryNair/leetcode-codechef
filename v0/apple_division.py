"""
There are n apples of known weights
Your task is to divide the apples into two group such that tge weight difference is minimal

"""

def divide_apples(weights, n):
    # For an array of size n, we can have 2**n ways
    # Of selecting a set of items from the array

    # We'll run through all these 2**n possibile sets 
    # & calculate sum of each set

    # sum all elements in the array; call this total_sum

    # We then check if the sum of current set (current_sum) is less than or equal to total_sum/2 
    # Best case scenario current_sum = total_sum
    # If not we register current sum & keep looking for a higher value of current_sum that is lesser that s/2
    # This way we refine our output by reducing the difference between two set sums

    total_sum = 0
    for weight in weights:
        total_sum += weight
    ans = 0

    for i in range(1<<n): # 1<<n == 2**n # Bitmask creation in this loop
        current_sum = 0
        for j in range(n): # Iteration of bitmask in this loop
            # Consider n = 3 <1 2 3>
            # Consider bitmask 001 or i = 1
            # As per this bitmask current set has to have element 3 
            # which is index 0
            # So if we take bitmask & shift it 0 times and bit AND by 1
            # Output should be 1

            # If bitmask was 101
            # 101 >> 0 & 1 as well as 101 >> 2 would be 1
            # So indices 0 & 2 to be added to set
            if i>>j&1:
                current_sum += weights[j]

        if current_sum <= total_sum/2: # check if this bitmask is any better than previous ones
            # select whichever is greater
            # previous current_sum or new one
            # so that difference between total_sum/2 
            # & current_sum is least

            # ans + diff = total_sum/2; diff needs to be min

            ans = max(ans, current_sum)
    
    print(total_sum - 2*ans) # ans + diff = total_sum/2; diff = total_sum - 2*ans

if __name__ == "__main__":
    n = 5 # number of apples
    weights = [3, 2, 7, 4, 1] # weight of each apple

    divide_apples(weights, n)



