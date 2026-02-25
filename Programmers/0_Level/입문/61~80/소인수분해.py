def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            answer.append(d)
            n = n // d
        else:
            d += 1
    print(answer)
    print(list(dict.fromkeys(answer)))
    return list(dict.fromkeys(answer))