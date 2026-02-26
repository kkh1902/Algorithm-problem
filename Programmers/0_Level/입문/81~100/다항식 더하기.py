def solution(polynomial):
    # x항과 상수항을 따로 저장할 변수
    x_term = 0
    constant_term = 0
    
    # polynomial을 " + " 기준으로 나누어 각 항을 처리
    terms = polynomial.split(" + ")
    
    for term in terms:
        # 항이 x가 포함된 경우
        if 'x' in term:
            # "x"만 있으면 계수는 1, 숫자가 있으면 그 숫자가 계수
            if term == 'x':
                x_term += 1
            else:
                x_term += int(term.replace('x', ''))
        # 항이 상수인 경우
        else:
            constant_term += int(term)
    
    # 결과 문자열을 만듦
    result = []
    
    # x항 처리
    if x_term == 1:
        result.append("x")
    elif x_term > 1:
        result.append(f"{x_term}x")
    
    # 상수항 처리
    if constant_term > 0:
        result.append(f"{constant_term}")
    
    # 리스트를 " + "로 합침
    return " + ".join(result)

