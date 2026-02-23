def solution(n):
    answer = 0
    
    for ch in str(n):  # 정수를 문자열로 변환
        answer += int(ch)
        
    return answer