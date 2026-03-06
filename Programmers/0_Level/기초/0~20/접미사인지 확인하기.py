def solution(my_string, is_suffix):
    ## 접미사를 다나눈다.
    ## is_suffix 가 그 리스트에 퐇람되냐 max가 my_string 의 길이
    answer = 0
    zub_list= []
    for i in range(len(my_string)):
        zub_list.append(my_string[-i:])
    
    if is_suffix in zub_list:
        answer=1

    
    return answer