coefficients = list(map(int,input().split()))
X = int(input())
calculatedPolymony= []
coefficients.reverse()
for i, n in enumerate(coefficients):
    calculatedPolymony.append(n*(X**i))
print(sum(calculatedPolymony))
