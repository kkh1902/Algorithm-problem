def solution(board):
    answer = 0

    for col in range(len(board)):
        for row in range(len(board[col])):
            if board[row][col] == 1:
                for j in range(max(col-1,0),min(col+2,len(board))):
                    for i in range(max(row-1,0),min(row+2,len(board))):
                        if board[i][j] == 1:
                            continue
                        board[i][j] = -1
    for i in board:
        answer += i.count(0)

    return answer


def solution(board):
    n = len(board)
    danger_zone = [[0] * n for _ in range(n)]  # 위험지역을 기록할 새로운 2차원 배열
    
    # 8방향(위, 아래, 좌, 우, 대각선) 이동을 위한 좌표
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # 지뢰가 있는 위치를 찾아서 그 주변을 위험지역으로 표시
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 지뢰 발견
                danger_zone[i][j] = 1  # 지뢰 자체도 위험지역으로 마킹
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < n and 0 <= nj < n:  # 배열의 범위를 벗어나지 않도록 확인
                        danger_zone[ni][nj] = 1
    
    # 위험지역이 아닌 안전한 지역의 칸 수를 계산
    safe_count = 0
    for i in range(n):
        for j in range(n):
            if danger_zone[i][j] == 0:  # 위험지역이 아니라면
                safe_count += 1
    
    return safe_count