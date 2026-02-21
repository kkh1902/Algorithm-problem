"""
문제 번호: 2470
문제 이름: 두 용액

1️⃣ 아이디어
- 정렬 + 투포인터 사용
- 가장 왼쪽(음수 쪽)과 가장 오른쪽(양수 쪽)에서 시작
- 두 수의 합을 계산
    - 합의 절댓값이 최소이면 정답 갱신
    - 합이 0보다 크면 → 값이 너무 큼 → right 감소
    - 합이 0보다 작으면 → 값이 너무 작음 → left 증가
- left < right 동안 반복

핵심:
✔ 이동 기준은 "합의 부호"
✔ 최소값 갱신은 "절댓값"

2. 시간복잡도
- for문 O(N^2) = 10^10 X
- Combination O(N^2) = 10^10 
- 정렬 + Twopointer O(N long N ) = 10^5 x log(10^5) = 10^5 * 17  가능
    -정렬 : O(N log N) + O(N)

3. 자료구조
- N: 용액 개수 (2 ≤ N ≤ 100,000)
- liquid: 용액 특성값 리스트 (음수/양수 모두 가능)
- min_yong : int (변수이름 어떻게 할까)
- left, right: 투포인터 인덱스
- min_val: 0에 가장 가까운 합의 절댓값
- answer: 정답이 되는 두 용액 값
"""


import sys

input = sys.stdin.readline
INF = float('inf')

N = int(input())
liquid = list(map(int, input().split()))

# 1. 정렬 (투포인터 사용을 위해 필수)
liquid.sort()

left = 0
right = N - 1

min_val = INF
answer = (0, 0)

# 2. left < right 동안 반복
while left < right:
    total = liquid[left] + liquid[right]

    # 3. 절댓값이 최소인지 확인 → 정답 갱신
    if abs(total) < min_val:
        min_val = abs(total)
        answer = (liquid[left], liquid[right])

    # 4. 합의 부호에 따라 포인터 이동
    if total > 0:
        right -= 1      # 값이 너무 크므로 줄이기
    elif total < 0:
        left += 1       # 값이 너무 작으므로 키우기
    else:
        break           # total == 0 이면 최적해

# 5. 결과 출력
print(answer[0], answer[1])