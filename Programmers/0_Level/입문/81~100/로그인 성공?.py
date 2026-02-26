def solution(id_pw, db):
    answer = ''
    cnt = 0
    max_cnt = len(db)
    pw_cnt = 0
    
    for i in db:
        if id_pw[0] == i[0]:
            # 아이디와 비번이 같은경우
            if id_pw[1] == i[1]:
                return "login"
            # 아이디는 같지만 비번이 다른경우
            else:
                pw_cnt+=1
        #아이디와 비번이 다 다른 경우
        else:
            cnt+=1
         
    if pw_cnt>=1:
        return "wrong pw"               
    if max_cnt == cnt:
        return "fail"
