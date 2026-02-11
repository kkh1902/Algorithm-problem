n = int(input())

left = 0
right = n
mid = 0
ans = 0 

while left<=right:
    mid = (left+right)//2
    if mid * mid  >=n:
        ans= mid
        right = mid- 1
    else:
        left= mid +1

print(ans)