n1, n2, n3 = (map(int, input().split()))
ma = max(n1, n2, n3)

if n1 >= 727 or n2 >= 727 or n3 >= 727:
   print("Error")    
elif n1 <= 94 or n2 <= 94 or n3 <= 94:
   print("Error")
else:    
   print(ma)    