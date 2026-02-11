"""
1. 아이디어
- 재귀로 피보나치를 호출하면 0과 1이 몇 번 출력되는지가 중요
- fibonacci(n)은 fibonacci(n-1)과 fibonacci(n-2)를 호출함
- 따라서 0과 1의 출력 횟수도 피보나치 규칙을 그대로 따름
- dp[n]에 n을 호출했을 때 (0 출력 횟수, 1 출력 횟수)를 저장
- 미리 0~40까지 DP로 계산해두고, 테스트케이스마다 바로 출력

2. 시간복잡도
- DP 사전 계산: O(40) → 상수 시간
- 테스트케이스 처리: O(T)
- 전체 시간복잡도: O(T)

3. 자료구조
- 2차원 리스트 dp
- dp[n] = [0 출력 횟수, 1 출력 횟수]
"""

import sys
input = sys.stdin.readline

T = int(input())

# dp[n] = [0 출력 횟수, 1 출력 횟수]
dp = [[0, 0] for _ in range(41)]

# 초기값
dp[0] = [1, 0]
dp[1] = [0, 1]

# DP 채우기
for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

# 테스트 케이스 처리
for _ in range(T):
    n = int(input())
    print(dp[n][0], dp[n][1])
