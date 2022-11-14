k = int(input())

for i in range(k):
    x = int(input())
    strxp = str(x + 1)
    strxm = str(x - 1)
    if len(strxp) != 6:
        strxp = strxp.zfill(6)

    if len(strxm) != 6:
        strxm = strxm.zfill(6)
    
    if int(strxp[0]) + int(strxp[1]) + int(strxp[2]) == int(strxp[3]) + int(strxp[4]) + int(strxp[5]):
        print("Yes")
    elif int(strxm[0]) + int(strxm[1]) + int(strxm[2]) == int(strxm[3]) + int(strxm[4]) + int(strxm[5]):
        print("Yes")
    else:
        print("No")