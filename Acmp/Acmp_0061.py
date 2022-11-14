k1 = 0
k2 = 0
a, b = map(int,input().split())
a1, b1 = map(int,input().split())
a2, b2 = map(int,input().split())
a3, b3 = map(int,input().split())
k1 = a + a1 + a2 + a3
k2 = b + b1 + b2 + b3

if k1 > k2:
    print(1)
if k1 < k2:
    print(2)
if k1 == k2:
    print("DRAW")