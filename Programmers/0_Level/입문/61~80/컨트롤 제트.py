def solution(s):
    arr = s.split(' ')
    result =[]
    for i in arr :
        if i=='Z':
            result.pop()
        else:
            result.append(int(i))
    return sum(result)