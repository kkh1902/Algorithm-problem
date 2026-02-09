a,b,c, m = list(map(int,input().split()))
ans= 0
p=0 
hour =0

for i in range(1,25):
    if p+a <=m:
        ans+=b
        p+=a
    else:
        p = max(0, p-c)


print(ans)