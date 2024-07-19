def countSpecialSubsequences(nums):
    MOD = 10**9 + 7
    count0, count1, count2 = 0, 0, 0

    for num in nums:
        if num == 0:
            
            count0 = (2 * count0 + 1) % MOD
        elif num == 1:
           
            count1 = (2 * count1 + count0) % MOD
        elif num == 2:
           
            count2 = (2 * count2 + count1) % MOD
    
    return count2


print(countSpecialSubsequences([0,1,2,2]))  
print(countSpecialSubsequences([2,2,0,0]))  
print(countSpecialSubsequences([0,1,2,0,1,2])) 
