import math

def solution(a, b):
    # a와 b의 최대공약수 (GCD) 구하기
    gcd = math.gcd(a, b)
    
    # 기약분수로 만들기
    b //= gcd
    
    # b가 2와 5로만 나눠지는지 확인
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    
    # b가 1이면 유한소수, 아니면 무한소수
    if b == 1:
        return 1
    else:
        return 2
