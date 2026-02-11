"""
문제번호 : 9663
문제이름 : N-Queen

1. 아이디어
- 한 행(row)에 퀸은 하나만 놓는다.
- row를 하나씩 증가시키며 가능한 열(col)에 퀸을 배치한다.
- 이미 사용한 열, 대각선에 퀸이 있다면 배치하지 않는다.
- 불가능해지면 이전 상태로 되돌아가는 백트래킹 사용.

2. 시간복잡도
- 최악의 경우 O(N!)
- 하지만 열 / 대각선 체크로 탐색 가지치기가 되어 실제 연산은 훨씬 줄어든다.

3. 자료구조
- col[i] : i번 열에 퀸이 있는지
- diag1[i] : (row + col) 대각선 여부
- diag2[i] : (row - col + N - 1) 대각선 여부
- cnt : 가능한 경우의 수
"""

import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

# 열과 대각선 방문 체크 배열
col = [False] * N
diag1 = [False] * (2 * N - 1)   # row + col
diag2 = [False] * (2 * N - 1)   # row - col + N - 1

def dfs(row):
    global cnt
    
    # 모든 행에 퀸을 다 배치한 경우
    if row == N:
        cnt += 1
        return
    
    # 현재 행(row)에 대해 모든 열(col) 시도
    for c in range(N):
        # 열, 두 대각선 모두 비어 있다면
        if not col[c] and not diag1[row + c] and not diag2[row - c + N - 1]:
            # 퀸 배치
            col[c] = True
            diag1[row + c] = True
            diag2[row - c + N - 1] = True
            
            dfs(row + 1)
            
            # 백트래킹 (원상복구)
            col[c] = False
            diag1[row + c] = False
            diag2[row - c + N - 1] = False

dfs(0)
print(cnt)
