"""
1. 아이디어
- 투포인터 
- 갯수 카운트 오른쪽으로 범위늘려가고 왼쪽 줄여가면서
- for 문 사용 다음인덱스더해주고 , 이전 인덱스빼주고

2. 시간복잡도
- O(N)? N(1 ≤ N ≤ 10,000),
right: 0 → N-1 (N번)
left: 0 → N-1 (N번)
총 이동 횟수 ≤ 2N → O(N)

3. 자료구조
- N, M : int  N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)
- nums : []
- cnt : int
- total : int
"""


import sys
input = sys.stdin.readline


N, M = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
left= 0
total = 0



# 다음 인덱스 더해주고, 이전 인덱스 빼주기
for right in range(N):
    total += nums[right]

    while total>=M:
        if total== M:
            cnt+=1
        total-=nums[left]
        left+=1

print(cnt)
    
