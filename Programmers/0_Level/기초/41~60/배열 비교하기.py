def solution(arr1, arr2):
    # 아이디어
    ## 우선순위에 따라
    ### 길이가 긴 경우  1
    ### 길이가 같은 경우 합 비교
    ### 길이가 같고 합도 같다면 0
    answer = 0
    
    arr1len= len(arr1)
    arr2len= len(arr2)
    
    if arr1len > arr2len:
        answer = 1
    elif arr2len > arr1len:
        answer = -1
    else:
        if sum(arr1)> sum(arr2):
            answer=1
        elif sum(arr2)> sum(arr1):
            answer = -1
        else:
            answer = 0
    
    return answer