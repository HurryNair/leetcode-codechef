def ContainsDuplicate(nums):
    seen = []
    for num in nums:
        if num in seen:
            return True
        else:
            seen.append(num)
    return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(ContainsDuplicate(nums))

