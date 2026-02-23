def solution(num_list):
    odd = 0
    Even = 0
    for i in num_list:
        if i % 2 == 0:
            Even +=1
        else:
            odd+=1
    return [Even, odd]