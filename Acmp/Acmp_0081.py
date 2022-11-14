n = int(input())
s = 0
t = 30000
x = list(map(int, input().split()))

for i in range(n):
    if x[i] < t:
        t = x[i]
    if x[i] > s:
        s = x[i]
print(t, s)