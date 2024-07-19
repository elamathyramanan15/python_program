def score_of_string(s: str) -> int:
    score = 0
   for i in range(1, len(s)):
        score += abs(ord(s[i]) - ord(s[i - 1]))
    return score

print(score_of_string("hello"))  
print(score_of_string("zaz"))    
