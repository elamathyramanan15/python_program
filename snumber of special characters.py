def count_special_letters(word: str) -> int:
    lower_set = set()
    upper_set = set()
    
    for char in word:
        if char.islower():
            lower_set.add(char)
        elif char.isupper():
            upper_set.add(char)
    
    special_count = 0
    for char in lower_set:
        if char.upper() in upper_set:
            special_count += 1
    
    return special_count

print(count_special_letters("aaAbcBC"))  
print(count_special_letters("abc"))  
print(count_special_letters("abBCab")) 
