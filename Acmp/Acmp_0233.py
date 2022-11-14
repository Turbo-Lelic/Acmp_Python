n = int(input())
n1 = list(map(int,input().split()))

var = 0

for i in range(n):
    if n1[i] <= 437:
        print ("Crash", int(i+1))
        var = 1
        break

if var == 0:
    print ("No crash")