text = input()
textelement = text.split()
max_n = len(textelement) - 1

n= 1
while n <= max_n :
    print(textelement[0] * int(textelement[n]))
    n = n + 1

