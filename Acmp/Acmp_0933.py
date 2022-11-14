a,b,c,t = map(int, input().split())

if t <= a:
    s = b * t
else:
    s = (a * b) + ((t - a) * c)

print(s)