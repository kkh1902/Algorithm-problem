def solution(common):
    # 공차 계산
    if common[1] - common[0] == common[2] - common[1]:
        # 등차수열
        d = common[1] - common[0]
        return common[-1] + d
    else:
        # 등비수열
        r = common[1] // common[0]
        return common[-1] * r
