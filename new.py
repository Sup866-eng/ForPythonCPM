import time
a = int(input())
b = int(input())
now1 = time.time()
for i in range(a, b+1):
    count = 0
    arr = []
    for j in range(2, b+1):
        if i % j == 0:
            count+=1
            arr.append(j)
    if count == 3:
        print("число: " + str(i) + "; " "делители:(" + str(1) + ", " + str(arr[0]) + ", " + str(arr[1]) + ", " + str(i) + ")")
print(time.time() - now1)