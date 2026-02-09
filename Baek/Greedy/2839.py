"""
1. 아이디어
- 그리디 알고리즘
- 5, 3 kg 봉지 저장 한뒤 5kg 봉지부터 최대한 사용 
-> 내리면서 딱맞을때까지 for문 돌리기

2. 시간복잡도
- O(N)

3. 자료구조
- 봉지 무게 : int[]
- 봉지 사용 cnt : int
- 남은 무게 : int

"""
import sys
input = sys.stdin.readline

n = int(input())
bags = [5, 3]
cnt = 0


# n 은 5로 나누어지면서 나머지가 3으로 나누어지면 딱맞는건데 이걸어떻게 로직으로 풀까
# 5kg 봉지 최대한 사용하면서 내려가기 range(n // 5, -1, -1)
# 3kg 봉지갯수도 count 해야함  나머지 remain = n- i*5
# n//5는 최대개수 여기서 부터 하나씩 줄이면서 확인  나머지가 3 으로 나누어지면  count
for i in range(n // 5, -1, -1):
    remain = n - (i * 5)
    if remain % 3 == 0:
        cnt = i + (remain // 3)
        print(cnt)
        break
else:
    print(-1)
    