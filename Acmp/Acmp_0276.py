x, y = list(map(int, input().split()))
div = x // y
mod = x % y

for i in range(y - mod):
    print(div)

for j in range(mod):
    print(div + 1)