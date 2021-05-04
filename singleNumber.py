class Solution:
    def singleNumber(self, nums: List[int]) -> int:
		d = {}
		for n in nums:
			if n not in d:
				d[n] = 1
			d[n] += 1
		return sorted(d.items(), key = lambda item : item[1])[0][0])
