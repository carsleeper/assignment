texts = list(input())
adds = []
romans = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
for i,word in enumerate(texts):
    texts[i] = romans[word]
def opr(arg):
    if len(arg) == 0:
        return None
    if len(arg) == 1:
        adds.append(arg[0])
        del arg[0]
    elif arg[0] < arg[1]:
        var = arg[1]-arg[0]
        adds.append(var)
        del arg[0]
        del arg[0]
    else:
        adds.append(arg[0])
        del arg[0]
    return opr(arg)
opr(texts)
print(sum(adds))
