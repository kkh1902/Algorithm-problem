import math
def solution(n):
    answer = 0
    while math.factorial(answer)<=n:
        answer+=1

    return answer -1