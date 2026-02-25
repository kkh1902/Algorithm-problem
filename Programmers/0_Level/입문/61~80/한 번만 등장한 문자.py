def solution(s):
    answer = ''
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if s.count(c) == 1:
            answer += c
    return answer

def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer