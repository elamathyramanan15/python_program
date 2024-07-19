from itertools import permutations

def maxCompatibilitySum(students, mentors):
    def compatibility_score(student, mentor):
        return sum(s == m for s, m in zip(student, mentor))

    m = len(students)
    max_score = 0

    for perm in permutations(range(m)):
        current_score = 0
        for i in range(m):
            student = students[i]
            mentor = mentors[perm[i]]
            current_score += compatibility_score(student, mentor)
        max_score = max(max_score, current_score)

    return max_score

print(maxCompatibilitySum([[1,1,0],[1,0,1],[0,0,1]], [[1,0,0],[0,0,1],[1,1,0]])) 
print(maxCompatibilitySum([[0,0],[0,0],[0,0]], [[1,1],[1,1],[1,1]])) 
