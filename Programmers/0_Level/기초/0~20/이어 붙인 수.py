def solution(num_list):
    odd = ""
    even = ""
    answer = 0
    for i in num_list:
        if i % 2==0:
            even += str(i)
        else:
            odd += str(i)
    
    print(even, odd)
    answer = int(odd) + int(even)
    return answer