def moveZeroes(nums):

    i = 0
    j = 0
    n = len(nums)
    while i<n:
        if nums[i]!=0:
            nums[i],nums[j] = nums[j],nums[i]
            j+=1
        i+=1
    return nums
moveZeroes([0, 1, 0, 3, 12])  # Example usage