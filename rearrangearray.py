def rearrangeArray(nums):
    nums.sort()
    n = len(nums)
    first_half = nums[:n//2]
    second_half = nums[n//2:]
    
    result = []
    i = 0
    j = 0
    while i < len(first_half) and j < len(second_half):
        result.append(first_half[i])
        result.append(second_half[j])
        i += 1
        j += 1

    while i < len(first_half):
        result.append(first_half[i])
        i += 1

    while j < len(second_half):
        result.append(second_half[j])
        j += 1

    return result


print(rearrangeArray([1, 2, 3, 4, 5])) 
print(rearrangeArray([6, 2, 0, 9, 7])) 
