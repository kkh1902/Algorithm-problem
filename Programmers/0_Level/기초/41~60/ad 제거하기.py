def solution(strArr):
    answer = []
    for i in strArr:
        if "ad" in i:
            strArr.remove(i)
    return strArr

def solution(strArr):
    return [i for i in strArr if "ad" not in i]