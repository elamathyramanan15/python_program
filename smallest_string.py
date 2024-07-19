def lexicographically_smallest_string(s: str, k: int) -> str:
    n = len(s)
    t = list(s)
    
    for i in range(n):
        cost = min(abs(ord(t[i]) - ord('a')), 26 - abs(ord(t[i]) - ord('a')))
        if k >= cost:
            t[i] = 'a'
            k -= cost
        else:
            break
    
    return ''.join(t)


print(lexicographically_smallest_string("zbbz", 3)) 
print(lexicographically_smallest_string("xaxcd", 4)) 
print(lexicographically_smallest_string("lol", 0))  
