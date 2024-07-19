def latest_time(s: str) -> str:
    if s[0] == '?':
        if s[1] == '?' or '0' <= s[1] <= '1':
            s = '1' + s[1:]
        else:
            s = '0' + s[1:]
            
    if s[1] == '?':
        if s[0] == '1':
            s = s[0] + '1' + s[2:]
        else:
            s = s[0] + '9' + s[2:]
    
    if s[3] == '?':
        s = s[:3] + '5' + s[4:]
        
    if s[4] == '?':
        s = s[:4] + '9'
    
    return s

print(latest_time("1?:?4"))  
print(latest_time("0?:5?"))  
