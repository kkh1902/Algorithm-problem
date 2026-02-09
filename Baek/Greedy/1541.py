"""
1. 아이디어
- 수식을 '-' 기준으로 나눈다
- 첫 번째 묶음은 그대로 더한다
- 두 번째 묶음부터는 내부의 '+' 연산 결과를 전부 빼준다
- 이렇게 하면 항상 최소값이 된다 (그리디)

2. 시간복잡도
- 문자열 분리 및 순회: O(N)
- N은 문자열 길이 (문제 조건상 매우 작음)

3. 자료구조
- 수식 문자열 리스트: List[str]
- 결과값 저장 변수: int
"""

import sys
input = sys.stdin.readline

# 입력 받기
expr = input().strip()

# '-' 기준으로 분리
parts = expr.split('-')

# 첫 번째 묶음 처리 (더하기)
result = 0
first_nums = parts[0].split('+')
for num in first_nums:
    result += int(num)

# 나머지 묶음들 처리 (전부 빼기)
for part in parts[1:]:
    nums = part.split('+')
    temp_sum = 0
    for num in nums:
        temp_sum += int(num)
    result -= temp_sum

# 결과 출력
print(result)
