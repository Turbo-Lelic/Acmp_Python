n, m, n_iskomii, m_iskomii = list(map(int, input().split()))
arr = [0] * n
x = 0

for i in range(n):
    arr[i] = [0] * m

for j in range(n):
    for l in range(m):
        arr[j][l] = x
        x += 1

for elem1 in range(n):
    if elem1 % 2 == 1:
        arr[elem1] = arr[elem1][::-1]
        
print(arr[n_iskomii - 1][m_iskomii - 1])