def solution(age):
    word = {'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
    answer= ''
    for i in str(age):
        answer+=word[i]
    return answer


def solution(age):

    return ''.join([chr(int(i)+97) for i in str(age)])


def solution(age):
    conv = {'0':'a','1':'b','2':'c','3':'d','4':'e'
            ,'5':'f','6':'g','7':'h','8':'i','9':'j'}
    return ''.join(conv[i] for i in str(age))