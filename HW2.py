array = list(map(int, input().split()))
s = int(input())
def binary_search(target):
    low = -1
    high = len(array)
    while low + 1 < high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess > target:
            high = mid
        else:
            low = mid
    if array[low] == target:
        return low
    return -1
def main(s):
    for i in range(0, len(array)):
        n = s - array[i]
        x = binary_search(n)
        if(x >= 0):
            print(array[i], array[x])
            break
main(s)