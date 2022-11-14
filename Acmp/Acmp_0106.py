n = int(input())
q = 0
a = 0

for i in range(n):
    x = input()
    if x == '0':
        q += 1
    else:
        a += 1 
    
if a >= q:
   print(q)
elif q >= a:
   print(a)