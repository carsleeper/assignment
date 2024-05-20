diameter = []
def mkdiameter(F,N):
    for i in range(F,F+N+1):
        diameter.append(int(i))
length = int(input())
li = input().split()
mkdiameter(li[0], length)
for i, num in enumerate(length):
    if num not in diameter:
        print(i)