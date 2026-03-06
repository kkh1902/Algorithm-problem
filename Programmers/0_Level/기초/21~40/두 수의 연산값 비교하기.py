def solution(a, b):
    answer = 0
    st1 = int(str(a)+ str(b))
    st2 = 2 * a * b
    
    if st1 >= st2:
        answer = st1
    else:
        answer = st2
    return answer