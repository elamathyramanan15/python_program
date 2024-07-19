from collections import Counter

def min_operations(grid):
    m, n = len(grid), len(grid[0])
    operations = 0
    
    for j in range(n):
        column = [grid[i][j] for i in range(m)]
        most_common = Counter(column).most_common(1)[0][0]
        
        for i in range(m):
            if grid[i][j] != most_common:
                grid[i][j] = most_common
                operations += 1
    
    for i in range(m):
        for j in range(n - 1):
            if grid[i][j] == grid[i][j + 1]:
                for value in range(10):  # 0 to 9 are valid values
                    if (j == 0 or grid[i][j - 1] != value) and (j == n - 2 or grid[i][j + 2] != value):
                        grid[i][j + 1] = value
                        operations += 1
                        break

    return operations


print(min_operations([[1, 0, 2], [1, 0, 2]])) 
print(min_operations([[1, 1, 1], [0, 0, 0]]))  
print(min_operations([[1], [2], [3]]))         
