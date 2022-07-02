class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            #First item will be unique
            #Check if second item is unique
            #In comparison to first
            #If not replace with next unique item
            #Repeat
            i = 1 
            for j in range(1, len(nums)):
                if nums[j] != nums[j-1]:
                    nums[i] = nums[j]
                    i += 1
        return i