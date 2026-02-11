"""
1. 아이디어
- 그리디 알고리즘
- 종료 시간이 가장 빠른 회의부터 선택
- 이전 회의가 끝난 이후에 시작할 수 있는 회의만 선택

2. 시간복잡도
- 입력: O(N)
- 정렬: O(N log N)
- 선택 과정: O(N) 
- 전체: O(N log N) ≈ 1,700,000 (약 170만) < 2억 가능

3. 자료구조
- 회의 수 : int (1<=N<=100,000)
- 회의 시작 시간 , 끝나는 시간 : int[][]
- 회의의 최대 개수 : int 
- 회의 시작 시간 ,끝시간 : int


"""
import sys
input = sys.stdin.readline

N = int(input())
times = []

for i in range(N):
    a,b = map(int,input().split())
    times.append([a,b])

times = sorted(times, key=lambda x: (x[1], x[0]))

end= 0
cnt =0

for s , e in times:
    if s >=end:
        cnt+=1
        end = e

print(cnt)