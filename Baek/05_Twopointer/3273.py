"""
1. 아이디어
- Twopointer 사용
- 한개 클릭 다른 한개 n+1 ~ j까지 2줄 for 문 X -> while문

2. 시간복잡도
- combination 사용할려고했으나 시간복잡도 O(?) 겠으나 시간 오바 판정
- for 문 사용하려고 했으나 이것 또한 시간 오바 O (N * (M)) 10만 * 10만  오바
- Two pointer 10만 + 10만 = 20만 가능

3. 자료구조
N : int 서로 다른 양의 정수
nums : [] n개의 양의 정수 리스트
K : int
left , right : int ->right <1000000
total: int
cnt : int

"""
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
K = int(input())

left = 0
right = N - 1
cnt =0

nums.sort()

while left < right:
    # 값보다 작을경우 왼쪽 증가
    if nums[left] + nums[right] < K :
        left+=1
    # 값보다 클경우 오른쪽 감소
    elif nums[left] + nums[right] > K :
        right-=1
    else: 
        # 그쌍은 버리고 안쪽으로 이동해야한다.
        cnt+=1
        left+=1
        right-=1

print(cnt)


