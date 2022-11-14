G = 'G'
C = 'C'
V = 'V'
I = 0
K = int(input())

while I < K:
    V, C = C, V
    G, C = C, G
    I+=1

print(G, C, V, sep="") 