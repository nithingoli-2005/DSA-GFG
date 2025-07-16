def second_largest(nums):
    if len(nums) < 2:
        return -1  # Not enough elements to find the second largest

    first = second = float('-inf')
    
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
            
    return second if second != float('-inf') else -1