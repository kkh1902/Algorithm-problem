def solution(score):
    answer = []
    li = []
    for i in score:
        li.append(sum(i)/len(i))
        
    sort_arr = sorted(li, reverse = True)
    
    for i in li:
        answer.append(sort_arr.index(i)+1)
        
    return answer