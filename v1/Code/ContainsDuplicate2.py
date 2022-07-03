def containsNearbyDuplicate(nums, k):
    o = {}
    for i in range(len(nums)):
        if nums[i] in o:
            o[nums[i]].append(i)
        else:
            o[nums[i]] = []
            o[nums[i]].append(i)
    
    for num in o:
        if len(o[num]) > 1:
            for i in range(0, len(o[num])-1):
                for j in range(i+1, len(o[num])):
                    if(abs(o[num][i] - o[num][j])) <= k:
                        return True
    
    return False

def containsNearbyDuplicateImproved(nums, k):
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen:
            if abs(seen[nums[i]] - i) <= k:
                return True
        seen[nums[i]] = i
    
    return False

if __name__ == "__main__":
    nums = [4,1,2,3,1,5]
    k = 3
    print(containsNearbyDuplicateImproved(nums, k))