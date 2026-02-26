def solution(num, total):
     # 시작 숫자 계산
    start = (total - (num * (num - 1)) // 2) // num
    # 연속된 num개의 숫자 리스트 생성
    return [start + i for i in range(num)]