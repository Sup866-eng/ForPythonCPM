try:
    a,b = map(int, input().split())
    isinstance(a, int)
    isinstance(b, int)
    for i in range(a, b+1):
        count = 0
        arr = []
        for j in range(2, b+1):
            if i % j == 0:
                count+=1
                arr.append(j)
        if count == 3:
            print("число: " + str(i) + "; " "делители:(" + str(arr[-1]) + ", " + str(arr[1]) + ", " + str(arr[0]) + ", " + str(1) + ")")
except:
    print("Это не числа, попробуйте еще раз, пожалуйста")
