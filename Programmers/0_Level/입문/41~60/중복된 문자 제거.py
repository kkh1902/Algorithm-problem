def solution(my_string):
    print(dict.fromkeys(my_string))
    return ''.join(dict.fromkeys(my_string))