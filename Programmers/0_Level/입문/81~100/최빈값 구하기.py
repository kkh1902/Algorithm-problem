def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1


def solution(array):
    answer = 0
    idx = [0] * 1001
    for i in array:
        idx[i] +=1
    if idx.count(max(idx)) >1:
        return -1
    return idx.index(max(idx))