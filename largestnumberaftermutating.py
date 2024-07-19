def maximumNumber(num, change):
    num_list = list(num)
    mutate = False
    n = len(num_list)
    
    for i in range(n):
        original_digit = int(num_list[i])
        mapped_digit = change[original_digit]
        
        if mapped_digit > original_digit:
            mutate = True
        
        if mutate:
            num_list[i] = str(mapped_digit)
           
            if mapped_digit < original_digit:
                mutate = False
    
    return ''.join(num_list)

print(maximumNumber("132", [9,8,5,0,3,6,4,2,6,8])) 
print(maximumNumber("021", [9,4,3,5,7,2,1,9,0,6]))  
print(maximumNumber("5", [1,4,7,5,3,2,5,6,9,4]))   
