"""
1. 아이디어
- 점화식 : a(n) = a(n-1) + a(n-2)
- n값 구하기 위해, for문 3부터 n까지 값을 구해주기
- 이전값, 이전이전값을더해서 , 10007로 나눈 나머지 저장

2. 시간 복잡도
- O(n) : n번 반복

3. 자료구조
- DP값 저장하는 (경우의 수 ) 배열 : int[]
    - 최대 값 : 10007보다 작음 > int

"""

import sys
input = sys.stdin.readline
n = int(input())

rs = [0,1,2]

for i in range(3,n+1):
    rs.append((rs[i-1] + rs[i-2]) % 10007)

print(rs[n])