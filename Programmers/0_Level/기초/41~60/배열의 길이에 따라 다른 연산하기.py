def solution(arr, n):
    ## 아이디어
    # 짝수인 경우
    # arrd의 길이 -1 해서 모든 경우를 나누어서 2로 나누어지는 것들을 배열에 넣는다
    # 그 배열에 해당되는 arr인덱스에 n을 더한다.
    # 홀수인 경우
    
    ## 시간복잡도
    ## 자료구조
    # 배열
    answer = []
    arrindex = []
    arrlen = len(arr)
    if arrlen %2==0:
        for i in range(arrlen):
            if i % 2 ==1:
                arrindex.append(i)
    else:
        for i in range(arrlen):
            if i % 2==0:
                arrindex.append(i)

    for i in arrindex:
        arr[i] = arr[i]+ n

    return arr