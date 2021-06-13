"""
Given an array arr[] consisting of N integers, where the ith element represents the range 
of a sprinkler i.e [i-arr[i], i+arr[i]] it can water, 
the task is to find the minimum number of the sprinkler to be turned on to water every plant 
at the gallery. If it is not possible to water every plant, then print -1.
Note: If arr[i] = -1, then the sprinkler cannot be turned on.
"""

def minSprinklers(sprinkler_ranges):

    n = len(sprinkler_ranges) # Number of spots in the garden that need watering
    min_coverage = 0 # Minimal point from where I need coverage i.e to the left; needs to be 0 or lesser
    max_coverage = 0 # maximum point of coverage i.e to the right; ideally n

    taps_open = 0 # number of open taps

    # We filter sprinklers that have left overage of value equal to or smaller than min
    # From the filtered list of sprinklers we pick the one with max range to the right
    # We then know that the garden patch from 0 to max_right_range is taken care of

    # We therefore set our current max to the next required min
    # Rinse and repeat until max_right_range is greate than n i.e. last stip on the right end of the garden
    while max_coverage < (n-1):

        # Iterate through the list
        # Filter sprinklers with left_range<=min
        for i in range(n): # [3,4,1,1,0,0]
            
            if ((i-sprinkler_ranges[i]) <= min_coverage and (i+sprinkler_ranges[i]) > max_coverage):
                max_coverage = i+sprinkler_ranges[i]
            
        # if we dont have an element that can take us farther right
        # or start from where we left off on the left
        # the if_condition will not pass 
        # Hence from previous iteration min will be equal to max

        if min_coverage == max_coverage:
            return -1

        # Otherwise, if there has been progress, open that tap 
        taps_open += 1

        min_coverage = max_coverage

    return taps_open

if __name__ == '__main__':
    sprinkler_ranges= [3,4,1,1,0,0]
    n = len(sprinkler_ranges)

    print(minSprinklers(sprinkler_ranges))
