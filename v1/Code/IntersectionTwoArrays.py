class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = {}
        for num in nums1:
            if num in n1:
                n1[num] += 1
            else:
                n1[num] = 1
        
        n2 = {}
        for num in nums2:
            if num in n2:
                n2[num] += 1
            else:
                n2[num] = 1
        
        res = []
        for number in n1:
            if number in n2:
                o = min(n1[number],n2[number])
                for i in range(o):
                    res.append(number)
        
        return res