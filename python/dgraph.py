SYM = input()
ASCIED_SYM = ord(SYM)
CHRED_SYM = chr(ord(SYM))
verti = chr(124)
space = chr(32)
blank = str()
#nums에 숫자들 분리해서 담기
nums = list(map(int,input().split()))
calcd_nums = list()

#이웃한 두 항의 차로 구성된 리스트 만들기
for i in range(len(nums)-1):
    calcd_nums.append(nums[i]-nums[i+1])
#출력
for i, n in enumerate(calcd_nums):
    #n가 음수일 때 출력
    if n < 0 :
        #공백출력
        if max(calcd_nums) < 0:
            print(verti, end=blank)
            for _ in range(-n):
                print(CHRED_SYM, end=blank)
        else :
            for _ in range(max(calcd_nums)):
                print(space, end = blank)
            # | 출력
            print(verti,end = blank)
            #기호 출력
            for _ in range(-n):
                print(CHRED_SYM, end = blank)
        #n가 0, 양수일 때 출력
    else : 
        for _ in range(max(calcd_nums)-n):
            print(space,end = blank)
        for _ in range(n):
            print(CHRED_SYM, end = blank)
        print(verti,end = blank)
    print("\n", end = blank)