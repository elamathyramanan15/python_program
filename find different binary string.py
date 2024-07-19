def findDifferentBinaryString(nums):
    n = len(nums)
    result = []
    
    for i in range(n):
        if nums[i][i] == '0':
            result.append('1')
        else:
            result.append('0')
    
    return ''.join(result)


print(findDifferentBinaryString(["01", "10"]))  
print(findDifferentBinaryString(["00", "01"]))  
print(findDifferentBinaryString(["111", "011", "001"]))  
