def solution(n, k):
    service_can_cnt = n//10
    answer = 0
    if n >=10:
        answer= n * 12000 + 2000 * (k-service_can_cnt)
    else:
        answer = n* 12000 + 2000 * k

    return answer