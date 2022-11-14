n = int(input())
maxx = n * 6
minn = n

if n % 6 == 0:
    minn = n // 6

else:
    minn = n // 6 + (7 - n % 6)

print(minn, maxx)