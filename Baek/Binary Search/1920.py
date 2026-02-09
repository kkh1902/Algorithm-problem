'''
1. 아이디어
- N개의 숫자를정렬
- M개의 for 돌면서, 이진탐색
- 이진탐색 안에서 마지막에 데이터 찾으면 1출력, 아니면 0 출력

2. 시간복잡도
- N개 입력값 정렬 = O(N log N)
- M개 이진탐색 = O(M log N)
- 총 O((N + M) log N) : 200,000 * log 200,000 = 약 3,000,000 < 2억
- 가능
- 그냥 for로 찾으면 O(N*M) : 200,000 * 200,000 = 40,000,000,000 > 2억 시간오바
-> 정렬 + 이진탐색

3. 자료구조
- N개 숫자 : int[]
- M개 숫자 : int[]

'''

# 문제 풀이 1 정렬 + 재귀 이진 탐색 (경계 수렴)
n= int(input())
nums= list(map(int, input().split()))

m= int(input())
target_list= list(map(int, input().split()))


nums.sort() # 이진 탐색 가능
# [4, 1, 5, 2, 3] -> [1, 2, 3, 4, 5]
# [1,3,7,9,5]


def search(st, en, target):
    if st == en:
        if nums[st] == target:
            print(1)
        else:
            print(0)
        return
    mid = (st + en) // 2
    # [1, 2, /3/, 4, 5] < [1,3,7,9,5]
    if nums[mid] < target:
        search(mid + 1, en,target)
    else:
        search(st, mid, target)

for each in target_list:
    search(0, n - 1, each)


# 다른 풀이 2 고전 이진 탐색 (while)
n = int(input())
nums = list(map(int, input().split()))
nums.sort()

m = int(input())
targets = list(map(int, input().split()))

def binary_search(nums, target):
    st, en = 0, len(nums) - 1
    while st <= en:
        mid = (st + en) // 2
        if nums[mid] == target:
            return 1
        elif nums[mid] < target:
            st = mid + 1
        else:
            en = mid - 1
    return 0

for t in targets:
    print(binary_search(nums, t))



# 다른 풀이 3 bisect 사용 (파이썬 내장)
import bisect

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

m = int(input())
targets = list(map(int, input().split()))

for t in targets:
    #  t이상이 처음으로 나오는 위치(인덱스)를 알려줌
    idx = bisect.bisect_left(nums, t)
    # 리스트 범위 안이냐?  그리고 그 위치의 값이 t이냐?
    if idx < n and nums[idx] == t:
        print(1)
    else:
        print(0)

'''
| 함수             | 의미             |
| -------------- | -------------- |
| `bisect_left`  | t 이상 **처음 위치** |
| `bisect_right` | t 초과 **처음 위치** |
👉 존재 여부 판단은 무조건 left
'''