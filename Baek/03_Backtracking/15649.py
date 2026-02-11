"""
1. 아이디어
- 순열 문제이므로 순서가 중요
- visited 배열로 중복 선택 방지
- M개를 모두 선택하면 출력

2. 시간복잡도
- O(P(N, M) × M)

3. 자료구조
- 선택된 숫자 리스트
- 방문 여부 배열
- 재귀 호출 스택
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 현재 선택한 숫자들을 저장
arr = []

# 숫자 사용 여부 체크 (중복 선택 방지)
visited = [False] * (N + 1)

def backtrack():
    # M개를 모두 선택했으면 출력
    if len(arr) == M:
        print(*arr)
        return

    # 1부터 N까지 숫자 중에서 선택
    for i in range(1, N + 1):
        # 이미 사용한 숫자는 건너뜀
        if visited[i]:
            continue

        # 숫자 i 선택
        visited[i] = True
        arr.append(i)

        # 다음 숫자 선택 (재귀)
        backtrack()

        # 선택 취소 (되돌리기)
        arr.pop()
        visited[i] = False

# 백트래킹 시작
backtrack()

