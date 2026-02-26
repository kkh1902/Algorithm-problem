def solution(A, B):
    # A와 B가 처음부터 같으면 0을 반환
    if A == B:
        return 0
    
    # A를 오른쪽으로 최대 len(A)-1번 밀면서 B와 같은지 확인
    for cnt in range(1, len(A) + 1):
        # A를 한 칸 오른쪽으로 밀기
        A = A[-1] + A[:-1]
        if A == B:
            return cnt  # B와 같아지면 그때의 밀린 횟수 반환
    
    return -1  # 끝까지 밀어도 같아지지 않으면 -1
