def solution(n):
    count = 0  # 3x 마을에서 쓰는 숫자의 개수를 세는 변수
    num = 1  # 시작 숫자
    
    while True:
        # 숫자 num이 3의 배수이거나 숫자 3을 포함하면 넘어감
        if num % 3 == 0 or '3' in str(num):
            num += 1
            continue
        
        # 3x 마을에서 쓰는 숫자이면 개수 증가
        count += 1
        
        # 개수가 n에 도달하면 해당 숫자 반환
        if count == n:
            return num
        
        num += 1
