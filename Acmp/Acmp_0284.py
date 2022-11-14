n = int(input())
arr = list(map(int, input().split()))
m = int(input())

for i in range(m):
    a, b = map(int, input().split())

    for l in range(a - 1, b):
        print(arr[l], end=' ')

    print()        