def solution(num_list):
    # 짝수번째 값들 합
    # 홀수번째 값들 합
    sum_even = sum(num_list[0::2])
    sum_odd = sum(num_list[1::2])
    answer = 0
    answer= max(sum_even,sum_odd)
    return answer