import math

l, w, h = (map(int, input().split()))
print(math.ceil((w * h * 2 + l * h * 2 ) / 16))