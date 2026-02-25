def solution(bin1, bin2):
    bin11= int(bin1,2)
    print(bin11)
    bin22= int(bin2,2)
    print(bin22)
    bin3 = bin11 + bin22
    answer= bin(bin3)[2:]
    return answer