class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        sums_so_far = []
        for i in range(n-1):
            current_sum = nums[i] + nums[i+1]
            if current_sum in sums_so_far:
                return True
            else:
                sums_so_far.append(current_sum)
        return False