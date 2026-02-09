"""
1. 아이디어
- N개의 숫자를정렬
- M개의 for 돌면서, 이진탐색
- 이진탐색 안에서 마지막에 데이터 찾으면 dict:cnt+1 , 아니면 넘어가기

2. 시간복잡도
- N개 입력값 정렬 = O(N log N)
- M개 이진탐색 = O(M log N)
- N(1 ≤ N ≤ 500,000) N(1 ≤ N ≤ 500,000) 
- 총 O((N + M) log N) : O(1,000,000) log 500,000 =  = 19,000,000 < 2억
- 가능
- 그냥 for O(N*M) : 500,000 * 500,000 = 250,000,000,000 > 2억 시간 오바
- >정렬 + 이진탐색

3. 자료구조
- N개 숫자 : int[]
- M개 숫자 : int[]
- cnt : int
- 숫자 : dict {}

"""
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

m = int(input())
targets = list(map(int, input().split()))

def lower_bound(arr, target):
    st, en = 0, len(arr)
    while st < en:
        mid = (st + en) // 2
        if arr[mid] < target:
            st = mid + 1
        else:
            en = mid
    return st

def upper_bound(arr, target):
    st, en = 0, len(arr)
    while st < en:
        mid = (st + en) // 2
        if arr[mid] <= target:
            st = mid + 1
        else:
            en = mid
    return st

result = []
for t in targets:
    cnt = upper_bound(nums, t) - lower_bound(nums, t)
    result.append(str(cnt))

print(" ".join(result))




