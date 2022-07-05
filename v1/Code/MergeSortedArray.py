def merge(nums1, m, nums2, n):
    if len(n) == 0:
        return
    
    i = m-1
    j = n-1
    l = len(nums1)-1 # New index scale

    while i >=0 and j>=0:
        if nums1[i] >= nums2[j]:
            nums1[l] = nums1[i]
        
            l -= 1
            i -=1
        
        else:
            nums1[l] = nums2[j]
            l-=1
            j-=1
    
    while(i >= 0):
        nums1[l] = nums1[i]
        l -= 1
        i -= 1
    
    while(j >= 0):
        nums[l] = nums2[j]
        l -= 1
        j -= 1
