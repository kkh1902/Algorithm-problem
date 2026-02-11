n,m = map(int,input().split())
tree =list(map(int,input().split()))
left= 1
right = 1000000000

while left<=right:
    mid= (left+right)//2
    ans=0
    
    for i in tree:
        if i > mid:
            ans+= i-mid

    if ans >= m:
        left = mid +1
    else:
        right = mid -1
    

print(right)