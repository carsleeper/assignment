number = input()
list1 = number.split()
listint = list(map(int, list1))
listint.sort()
listintend = listint[:]
listintstart = listint[:]
del listintstart[0]
del listintend[-1]
startd = max(listintstart) - min(listintstart)
endd = max(listintend) - min(listintend)
if len(listint) == 1:
    print(0)
if startd >= endd :
    print(startd)
else :
    print(endd)
