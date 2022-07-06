class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        n1 = nums[0]
        for i in range(len(nums)):
            if nums[i] > n1:
                curr_diff = nums[i] - n1
                if curr_diff > max_diff:
                    max_diff = curr_diff
            else:
                n1 = nums[i]
        return max_diff