n = int(input())
m = list(map(int, input().split()))
c = []
hc = []

for i in range(n):
    if m[i] % 2 == 0:
        c.append(m[i])
        
    else:
        hc.append(m[i])
        
print(*hc)
print(*c)

if len(hc) > len(c):
    print("NO")
    
else:    
    print("YES")