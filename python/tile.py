import sys
x,y = map(int,input().split())
fib_memo = {}
#x,y중 큰 값보다 커질때 까지 피보나치 생성
def fib(n):
    if n in fib_memo:
        return fib_memo[n]
    result = 1 if n <= 1 else fib(n-1)+fib(n-2)
    fib_memo[n] = result
    return result
M = 0
while fib(M) < min(x,y):
    M += 1
if min(x,y) == 1:
    print(x*y if x == y or max(x,y) == 2 else 0)
    sys.exit()
if fib(M) ==  min(x,y) and fib(M-1)+fib(M) == max(x,y):
    print(x*y)
elif x == y == fib(M):
    print(x*y)
else:
    print(0)
