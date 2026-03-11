def solution(myString, pat):
    # pat이 myString의 연속된 부분 문자열에 속하면 1 아니면 0
    answer = 0
    myString = myString.lower()
    pat = pat.lower()
    if pat in myString:
        answer=1
    else:
        answer=0
    return answer