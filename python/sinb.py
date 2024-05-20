text = (input())
firstinput = int(text)
inset = {""}
text = (input())
while text != "" :
        inset.add(int(text))
        text = (input())

def square(n) :
    line = "+---" * n
    star = "| * "
    nostar = "|   "
    print(f"{line}+", sep = "")
    num = 1
    resultnum = n + 1 - num
    element = resultnum in inset
    if element == True :
        print(f"{nostar * (resultnum - 1)}{star}{nostar * (n - resultnum)}|", sep = "")
    else :
        print(f"{nostar * n}|", sep = "")
    print(f"{line}+", sep = "")
    while n > num :
        num = num + 1
        resultnum = n + 1 - num
        element = resultnum in inset
        if element == True :
            print(f"{nostar * (resultnum - 1)}{star}{nostar * (n - resultnum)}|", sep = "")
        else :
            print(f"{nostar * n}|", sep = "")
        aaaa = "+"
        print(f"{line}{aaaa}", sep = "")
square(firstinput)
