def solution(my_string):
    answer = ''
    vowels = 'aeiou'
    
    for ch in my_string:
        if ch not in vowels:
            answer += ch
            
    return answer
