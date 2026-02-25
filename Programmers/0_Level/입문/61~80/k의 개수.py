def solution(i, j, k):
    answer = 0
    li = [_ for _ in range(i,j+1)]
    num = list(map(str,li))
    ar = ''.join(num)   
    return ar.count(str(k))