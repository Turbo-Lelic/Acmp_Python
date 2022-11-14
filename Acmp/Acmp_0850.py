import math

a, b = map(int,input().split())
minn = int(math.ceil(max(a, b) / 2))
maxx = min(a, b)

print(minn, maxx)