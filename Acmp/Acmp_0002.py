n = int(input())
sum = 0

if n > 0:
    for i in range(1, n + 1):
        sum += i
else:
    for i in range(1, n - 1, -1):
        sum += i
        
print(sum)