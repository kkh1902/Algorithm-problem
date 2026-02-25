def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    print(before, after)
    if before==after:
        return 1
    else:
        return 0