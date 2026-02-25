def solution(emergency):
    answer = [0] *len(emergency)
    emergenci= sorted(emergency,reverse=True)
    for i in emergenci:
        answer[emergency.index(i)] = emergenci.index(i)+1
    
    return answer