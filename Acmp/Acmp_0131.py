n = int(input())
vmax = 0
ans = 0
 
for i in range(n):
    v, s = map(int, input().split())

    if s == 1:
        if v > vmax:
            vmax = v
            ans = i + 1
 
if ans == 0:
    print(-1)
else:
    print(ans)