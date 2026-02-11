n , k = map(int,input().split())
nk_list = [i for i in range(1,n+1)]
result = []
idx = k-1

while len(nk_list)!=0:
    result.append(nk_list.pop(idx))
    if len(nk_list)==0:
        break
    else:
        idx = (idx+k-1) %len(nk_list)


print("<" + ", ".join(map(str, result)) + ">")
