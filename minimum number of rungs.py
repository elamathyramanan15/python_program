def addRungs(rungs, dist):
    current_height = 0
    additional_rungs = 0

    for rung in rungs:
        if rung - current_height > dist:
            additional_rungs_needed = (rung - current_height - 1) // dist
            additional_rungs += additional_rungs_needed
        current_height = rung
    
    return additional_rungs


print(addRungs([1, 3, 5, 10], 2)) 
print(addRungs([3, 6, 8, 10], 3))  
print(addRungs([3, 4, 6, 7], 2)) 
