def solution(myString, pat):
    # 1. A를 B로, B를 A로 바꾸기
    transformed = myString.replace('A', 'X').replace('B', 'A').replace('X', 'B')
    
    # 2. 변환된 문자열에 pat이 있는지 확인
    if pat in transformed:
        return 1
    else:
        return 0
