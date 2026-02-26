def solution(babbling):
    # 발음할 수 있는 단어 목록
    valid_words = ["aya", "ye", "woo", "ma"]
    answer = 0

    # 각 단어를 확인
    for word in babbling:
        temp_word = word
        
        # 발음 가능한 단어들을 하나씩 치환
        for valid in valid_words:
            temp_word = temp_word.replace(valid, " ")

        # 치환 후 남은 문자열이 없으면 발음 가능한 단어로 간주
        if temp_word.strip() == "":
            answer += 1
    
    return answer
