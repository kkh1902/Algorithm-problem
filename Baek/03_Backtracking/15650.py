"""
1. 아이디어
- 조합 문제 (순서 중요하지 않음)
- 오름차순으로만 선택해야 하므로 start 인덱스를 사용
- 이전에 선택한 숫자보다 큰 숫자만 다음에 선택
- M개를 모두 선택하면 출력

2. 시간복잡도
- O(C(N, M) × M)

3. 자료구조
- 선택된 숫자를 저장하는 리스트
- 재귀 호출 스택
"""

import sys
input = sys.stdin.readline

# N: 1부터 N까지의 숫자
# M: 선택할 개수
N, M = map(int, input().split())

# 현재 선택한 숫자들을 저장하는 리스트
arr = []

def backtrack(start):
    # M개를 모두 선택했으면 출력
    if len(arr) == M:
        print(*arr)
        return

    # start부터 N까지 숫자 중에서 선택
    # start 이전 숫자는 이미 고려했으므로 중복 선택 방지
    for i in range(start, N + 1):
        # 숫자 i 선택
        arr.append(i)

        # 다음 숫자는 i보다 큰 수만 선택 가능
        backtrack(i + 1)

        # 선택 취소 (되돌리기)
        arr.pop()

# 백트래킹 시작 (1부터 선택)
backtrack(1)
