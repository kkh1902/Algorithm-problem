def solution(number, n, m):
    answer = 0
    if number % n ==0:
        if number % m ==0:
            return 1
        else:
            return 0
    else:
        return 0     
    

def solution(number, n, m):
    return 1 if number%n==0 and number%m==0 else 0   