def solution(slice, n):
    answer = (n+slice-1)//  slice
    # 나머지가 조금이라도 있으면 다음 몫 구간으로 밀어버리는 장치
    return answer