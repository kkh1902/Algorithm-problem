def solution(n, control):
    joystick = dict(zip(["w","a","s","d"],[1,-10,-1,10])    )         
    for i in control:
        n += joystick[i]
    return n