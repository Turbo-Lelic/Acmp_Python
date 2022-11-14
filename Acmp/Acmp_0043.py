x = list(map(str, input().split('1')))
maxx = 0

for i in range(len(x)):
    if len(x[i]) > maxx:
        maxx = len(x[i])

print(maxx)