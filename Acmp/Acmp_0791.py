s = int(input())
ans = []
 
if s - 8 >= 1:
    ans.append(s - 8)
 
if s + 8 <= 64:
    ans.append(s + 8)
 
if (s - 1) % 8 != 0 and s - 1 >= 1:
    ans.append(s - 1)
 
if s % 8 != 0 and s + 1 <= 64:
    ans.append(s + 1)
 
ans.sort()
 
print(*ans)