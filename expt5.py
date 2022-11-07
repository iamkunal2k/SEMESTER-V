import hmac
import hashlib


plaintext = input("Enter the plaintext : ")
key = "10000101"
print(key)
print("######################################################")


temp = [plaintext[element: element + 8]
        for element in range(0, len(plaintext), 8)]
matrix = [list(item) for item in temp]
print(matrix)
listnew =[]
for i in matrix:
    if len(i)<8:
        listlen = 8-len(i)
        for j in range(listlen):
            i.append("0")
    listnew.append(i)


print("-------After Arranging the plaintext in 8 bits and adding zeros-------")
print(listnew)

ipad = "01011100"
opad = "00110110"

#length of M
l = "00110000"
i_vector = "11001100"


print("-----------------------------------------------------------\n")
A_list = [(ord(a) ^ ord(b)) for a,b in zip(key, ipad)]
A_stringlist = [str(x) for x in A_list]


B_list = [(ord(a) ^ ord(b)) for a,b in zip(key, opad)]
B_stringlist = [str(x) for x in B_list]

print("------------------A and b in List---------------")
print(A_stringlist)
print(B_stringlist)

A = "".join(A_stringlist)
B = "".join(B_stringlist)



print("-------------------A and B String---------------")
print("A = ",A)
print("B = ",B)

iv_list = list(i_vector)
print("------------------------------------------------------------\n")

print("--------------------Values of Z----------------------")
z0 = "".join([i_vector, A])
print("Z0 = ",z0)

print(len(matrix))
print(matrix[0])
print("--------------------------------------------------------")

for i in range(len(matrix)) :
    m = "".join(matrix[i])
    print(m)

signature = hmac.new(
    z0,
    m,
    hashlib.sha256
).hexdigest()
print("signature: {}")

