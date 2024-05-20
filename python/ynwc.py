li = list(input().lower())
semivowel = ['w','y']
vowel = ['a','e','i','o','u']
alpha = {}
# [23.434, 43.235, 35,664]
li2 = []
#alpha 딕셔너리에 다 담기
for i, word in enumerate(li) :
    NUM = 1
    if word.isalpha() :
        if word not in alpha :
            alpha[word] =  NUM
        else :
            exi = alpha[word]
            exi += 1
            alpha[word] = exi
alphakey = list(alpha.keys())
#무게 측정
for i in range(len(alpha)) :
    if alphakey[i] in semivowel :
        li2.append((1.5)*(alpha[alphakey[i]]))
    elif alphakey[i] in vowel :
        li2.append(2.0*(alpha[alphakey[i]]))
    else :
        li2.append(1.0*(alpha[alphakey[i]]))
li3 = []
for i,number in enumerate(li2) :
    li3.append((number/sum(li2))*100)
m = max(li3)
print(f"{m:.3f}")
