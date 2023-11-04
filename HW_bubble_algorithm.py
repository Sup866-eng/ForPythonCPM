arr = map(int, input())
for i in range(1, len(arr)):
    for j in range(1, len(arr)):
        a = arr[j]
        b = arr[j+1]
        if a > b:
            a,b = b,a
for i in arr:
    print(arr[i])