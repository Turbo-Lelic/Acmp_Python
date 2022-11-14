room, acond = map(int, input().split())
a = input()
b = room

if a == "freeze":
    b = min(room, acond)
if a == "heat":
    b = max(room, acond)
if a == "auto":
    b = acond

print(b)