if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    bigger = arr[0]
    for i in range(0, n):
        if arr[i] > bigger:
            bigger = arr[i]
    print(bigger)