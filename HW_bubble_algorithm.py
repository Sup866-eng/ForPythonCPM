arr = list(map(int, input().split()))
for i in range(1, len(arr)):
    for j in range(1, len(arr)):
        if arr[j-1]>arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
print(arr)
