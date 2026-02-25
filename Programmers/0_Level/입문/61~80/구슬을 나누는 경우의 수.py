import math 
def solution(balls, share):
    nfac = math.factorial(balls)
    mfac = math.factorial(share)
    answer = nfac/(mfac * math.factorial(balls-share))
    
    return answer