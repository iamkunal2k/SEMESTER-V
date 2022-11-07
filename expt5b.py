import hashlib
pt = "1111100000011011111001000100101011101100110010"
key = "10000101"
ipad = "01011100"
opad = "00110110"
iv = "11001100"


def group(s):
    k = 8
    ll = 0
    hl = k
    lst = []

    for z in range(0, len(s)):
        lst.append(s[ll:hl])
        ll = hl
        hl += k
        while("" in lst):
            lst.remove("")

    if(len(lst[len(lst)-1]) != 8):
        n = 8-len(lst[len(lst)-1])
        str1 = lst[len(lst)-1]
        lst.remove(lst[len(lst)-1])
        for i in range(n):
            str1 += '0'
            lst.append(str1)
            return lst


def btod(num):
    lst = list(num)
    lst.reverse()
    decimal = 0
    for i in range(len(lst)):
        dec = int(lst[i])
        decimal = decimal + dec * pow(2, i)

    return(decimal)


def removeb(b):
    lstb = list((b))
    for i in range(len(lstb)):

        if lstb[i] == 'b':
            lstb[i] = '0'
            b = ''.join(lstb)
            return b


def check16bit(chk):
    if(len(chk) > 16):
        chk = chk[-15:]
        return chk


lst = group(pt)
M = ''.join(lst)
l = len(M)
bl = bin(l)
bl = removeb(bl)
# print((bl))
A = int(btod(key) ^ btod(ipad))
B = int(btod(key) ^ btod(opad))

A = bin(A)
A = removeb(A)
A = A[-8:]
B = bin(B)
B = removeb(B)
B = B[-8:]
# B=check8bit(B)
zn = []
z = iv+str(A)
zn.append(z)
# print(z)
Z = ""
for m in lst:
    Z = ""
    Z = (bin(int.from_bytes(hashlib.sha1(m.encode()).digest(), 'big'))[-8:])+m
    Z = removeb(Z)

    Z = check16bit(Z)
    zn.append(Z)

z = Z
Z = (bin(int.from_bytes(hashlib.sha1(z.encode()).digest(), 'big'))[-8:])+bl
Zk1 = removeb(Z)
Zk1 = check16bit(Zk1)
Z = (bin(int.from_bytes(hashlib.sha1(Zk1.encode()).digest(), 'big'))[-8:])
Z = removeb(Z)
Z = Z[-8:]
# print(Z)
P = iv+B
Q = (bin(int.from_bytes(hashlib.sha1(P.encode()).digest(), 'big'))[-8:])
Q = Q[-8:]
R = Q+Z
T = (bin(int.from_bytes(hashlib.sha1(R.encode()).digest(), 'big'))[-8:])
T = removeb(T)
print("M = ", M)
print("L = ", bl)
print("A = ", A)
print("B = ", B)
for i in range(len(zn)):
    print("Z", i, " = ", zn[i])

print("Z k+1 = ", Zk1)
print("Hash of Z k+1 = ", Z)
print("P = ", P)
print("Q = ", Q)
print("R = ", R)
print("T = ", T)
