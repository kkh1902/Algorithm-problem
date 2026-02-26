def solution(quiz):
    answer = []
    for i in quiz:
        dab = i.split("=")
        result = eval(dab[0])
        if result == int(dab[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer