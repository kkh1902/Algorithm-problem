def solution(arr, idx):
    answer = 0
    
    for index, arrs in enumerate(arr):
        if index > idx-1 and arrs ==1:
            answer= index
            break
        else:
            answer= -1

    return answer