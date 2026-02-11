word= input()

result = word.replace("XXXX", "AAAA").replace("XX", "BB")

if "X" in result:
    print(-1)
else:
    print(result)
