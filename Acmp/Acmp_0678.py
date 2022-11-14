a = input()
n1 = 1
n2 = 0
n3 = 0

for i in range(len(a)):
    if a[i] == "A":
        n1, n2 = n2, n1
    if a[i] == "B":
        n2, n3 = n3, n2
    if a[i] == "C":
        n1, n3 = n3, n1
if n1 == 1:
    print(1)
if n2 == 1:
    print(2)
if n3 == 1:
    print(3)