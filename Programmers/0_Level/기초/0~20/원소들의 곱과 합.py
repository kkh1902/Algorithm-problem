def solution(num_list):
    sumo = sum(num_list)
    sumx = 1
    for i in num_list:
        sumx *=i
    
    if sumx < sumo*sumo:
        return 1
    else:
        return 0