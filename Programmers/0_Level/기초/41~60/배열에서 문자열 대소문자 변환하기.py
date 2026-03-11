def solution(strArr):
    ## 모든 원소가 알파벳인 경우
    ### 배열 홀수번째 인덱스의 문자열은 모든 문자를 -> 대문자
    ### 배열 짝수번째 인덱스의 문자열은 모든 문자를 -> 소문자
    #### 홀수인덱스 -> 대문자
    #### 짝수인덱스 -> 소문자
    cnt = 0
    answer = []
    for i in strArr:
        if cnt %2==0:
            answer.append(i.lower())
        else:
            answer.append(i.upper())
        cnt+=1
        
    
    return answer