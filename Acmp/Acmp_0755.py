x, y, z = (map(int, input().split()))

if x + y >= z:
  print(x + y - z)
else:
  print("Impossible")