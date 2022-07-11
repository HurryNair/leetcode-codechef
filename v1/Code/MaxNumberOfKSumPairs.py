class Solution:
    def maxOperations(nums, k):
        seen = {}
        count = 0

        for num in nums:

            if k-num in seen:
                count += 1
                seen[k-num] -= 1
                if seen[k-num] == 0:
                    seen.pop(k-num)
                continue
            
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
            
            return count
