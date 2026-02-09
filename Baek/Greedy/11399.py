# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

"""
1. 아이디어
- time 리스트를 받아서 역순 정렬
- 누적합
2. 시간복잡도
- O(N)

3. 자료구조
- 사람수 : int
- time 리스트 : int []
- 합의 최솟값 : int

"""
# 문제 풀이 1  지금은 매번 sum()을 써서
# 👉 시간복잡도가 사실상 O(N²)
import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
rs= 0


time.sort()


for i in range(n):
    rs+= sum(time[0:i+1])

print(rs)


# 문제 풀이 2  누적합 변수 하나 추가
import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))

time.sort()    

cur = 0
rs = 0

for t in time:
    cur += t
    rs += cur

print(rs)