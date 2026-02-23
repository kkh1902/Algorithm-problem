def solution(my_string, n):
    answer = ''
    my= list(my_string)
    for i in my:
        answer += i *n
    return answer