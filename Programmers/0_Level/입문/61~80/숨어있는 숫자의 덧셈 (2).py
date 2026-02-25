def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    print(s)
    return sum(int(i) for i in s.split())