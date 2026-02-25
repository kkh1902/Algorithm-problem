def solution(sides):
    # n이 1씩 증가하면서 가장 긴변의 길이가 n으로 바뀌는 때를 기준으로
    # 이전에는 min(sides) - 1개의 삼각형을 만들수 있고
    # 이후로는 min(sides) 개의 삼각형을 만들 수 있음
    return 2*min(sides) - 1