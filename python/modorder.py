N = int(input())
rawList = list(map(int,input().split()))
def sort_func(li):
    if len(li) <= 1:
        return li
    x = li.pop(0)
    equal_big = [i for i in li if i%N >= x%N]
    small = [j for j in li if j%N < x%N]
    return sort_func(small) + [x] + sort_func(equal_big)
editedList = sort_func(rawList)
for w in editedList:
    print(f"{w} ", end ="")
