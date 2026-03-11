def solution(myString):
    split_myString = myString.split('x')
    print(split_myString)
    answer = []
    for j in split_myString:
        answer.append(len(j))
    return answer