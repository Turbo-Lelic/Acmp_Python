k,n = map(int,input().split())
a = 1
b = k
l = 1

while not(a <= n and n <= b):
    a += k
    b += k
    l += 1
    
print(l, n - a + 1)