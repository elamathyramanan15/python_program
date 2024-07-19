def isPrefixString(s, words):
    concatenated = ""
    
    for word in words:
        concatenated += word
        if concatenated == s:
            return True
        
        elif len(concatenated) > len(s):
            return False
    
    return False

print(isPrefixString("iloveleetcode", ["i","love","leetcode","apples"]))  
print(isPrefixString("iloveleetcode", ["apples","i","love","leetcode"]))  
