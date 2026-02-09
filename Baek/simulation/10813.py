"""
1. 아이디어
- 받아서 값을 교환 해준다
- x, y 로 받은 다음 교환 할예정 바로 교환 및 초기화 안될듯

2. 시간복잡도
- O(M)

3. 자료구조
- N, M : int N (1 ≤ N ≤ 100) M (1 ≤ M ≤ 100)
- basket : [] 0, 1,2 ,3,N  초기화 

"""
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# basket = [0] * (N+1)
# for i in range(N+1):
#     basket[i] = i

# for j in range (M):
#     a,b = map(int, input().split())
#     x = basket[a]
#     y = basket[b]
#     basket[a] = y
#     basket[b] = x


# print(* basket[1:N+1])


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = list(range(N + 1))

print(basket)
for _ in range(M):
    a, b = map(int, input().split())
    basket[a], basket[b] = basket[b], basket[a]

print(*basket[1:])
