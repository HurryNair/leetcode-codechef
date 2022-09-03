# Brute Force

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_vol = 0
#         for i in range(0, len(height)-1):
#             for j in range(i+1, len(height)):
#                 curr_vol = min(height[i], height[j])*(j-i)
#                 if curr_vol > max_vol:
#                     max_vol = curr_vol
        
#         return max_vol
                
#2 pointer approach
#               
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        l = 0
        r = len(height) - 1
        while l < r:
            curr_vol = min(height[l], height[r])*(r-l)
            if curr_vol > max_vol:
                max_vol = curr_vol
            
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return max_vol
                
                
        