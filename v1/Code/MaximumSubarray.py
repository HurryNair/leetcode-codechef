
def maxSubArray(self, nums: List[int]) -> int:
    max_so_far = float('-inf') - 1
    max_ending_here = 0
    
    for num in nums:
        max_ending_here = max_ending_here + num
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
        
        if max_ending_here < 0:
            max_ending_here = 0
        
    return max_so_far

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    maxSubArray(nums)