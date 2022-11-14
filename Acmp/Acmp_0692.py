x = int(input())
x1 = 1
x2 = 'NO'

while x >= x1:
    if x == x1:
        x2 = 'YES'
        break
    x1 *= 2
    
print(x2)