t1 = input()
h, m = map(int, input().split())
 
h_t1, m_t1 = map(int, t1.split(":"))
 
h_t1 += h
m_t1 += m
 
if m_t1 >= 60:
    m_t1 -= 60
    h_t1 += 1

h_t1 %= 24    
 
print(str(h_t1).zfill(2), ":", str(m_t1).zfill(2), sep='')