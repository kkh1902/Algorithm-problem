from itertools import combinations
def solution(numbers):
    maxv=0
    for a,b in combinations(numbers,2):
        maxv = max(maxv, a*b)
    return maxv