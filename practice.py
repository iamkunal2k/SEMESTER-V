import hmac
import hashlib
from pydoc import plain
plaintext = "1111100000011011111001000100101011101100110010"
temp = [plaintext[element: element + 8] for element in range(0,len(plaintext),8)]
matrix = [list(item) for item in temp]
print("\n------before adding zeroes------")
print(matrix)

listnew = []
for i in matrix:
    if len(i)<8:
        listlen = 8-len(i)
        for j in range(listlen):
            i.append('0')
    listnew.append(i)

print("\n-----after adding zeroes------")
print(listnew)
print(len(listnew))

list_decrypt= []
for i in range(len(listnew)):
    for j in range(8):
        list_decrypt.append(listnew[i][j])

print("\n--------final list---------")
print(list_decrypt)
input_final = "".join(list_decrypt)
print("\n--------final string---------")
print(input_final)
print("\n---------A and B-----------")
len_final = len(input_final)
# finallist = "".join(listnew)
# print(len(listnew))
# l = len(listnew)
ipad = '01011100'
opad = '00110110'
iv = '11001100'
key = '10000101'
L = '00110000'      # 48 in decimal (Length of string)

A = [(ord(key) ^ ord(ipad)) for key, ipad in zip(key, ipad)]
print(A)
B = [(ord(key) ^ ord(opad)) for key, opad in zip(key, opad)]
print(B)
print("\n---------IV LIST-----------")
iv_list = list(iv)
print(iv_list)
iv_string = "".join(iv_list)
print("\n-------A and B string list----------")
A_stringlist = [str(x) for x in A]
print(A_stringlist)
B_stringlist = [str(x) for x in B]
print(B_stringlist)

A_string = "".join(A_stringlist)
B_string = "".join(B_stringlist)

print("\n-----------A and B string------------")
print(A_string)
print(B_string)

# z0 = "".join([iv, A_string])
# print(z0)
# for i in range()
print("\n------------------Z values-----------------")
z0 = "".join([iv, A_string])
print("Z0 = ",z0)


hz0 = hashlib.new('ripemd160')
print("Hash of z0: ",hz0)

# hz0 = hash(z0)
# print(hz0)

bz0 = ''.join(format(ord(hz0),'b') for hz0 in z0)
# print("Binary value of hz0: ",bz0)
# print(type(bz0))
# print(len(bz0))
z1 = bz0[-8:] + "".join(listnew[0])
print("Z1 = ",z1)

decimal_representation = int(z1, 2)
hexadecimal_string = hex(decimal_representation)
print("The hex value of Z1 = ",hexadecimal_string)

#--------------------------z2------------------------------
hz1 = hashlib.new('ripemd160')
print("Hash of z1 : ",hz1)

bz1 = ''.join(format(ord(hz1),'b') for hz1 in z1)
# print("Binary value of hz1 : ",bz1)

z2 = bz1[-8:] + "".join(listnew[1])
# print("Z2 = ",z2)
decimal_representation = int(z2, 2)
hexadecimal_string = hex(decimal_representation)
print("The hex value of Z2 = ",hexadecimal_string)


# #--------------------------z3------------------------------
# hz2 = hashlib.new('ripemd160')
# print("Hash of z2 : ",hz2)

# bz2 = ''.join(format(ord(hz2),'b') for hz2 in z2)
# # print("Binary value of hz2 : ",bz2)

# z3 = bz2 + "".join(listnew[2])
# # print("Z3 = ",z3)
# decimal_representation = int(z3, 2)
# hexadecimal_string = hex(decimal_representation)
# print("The hex value of Z3 = ",hexadecimal_string)

# #--------------------------z4------------------------------
# hz3 = hashlib.new('ripemd160')
# print("Hash of z3 : ",hz3)

# bz3 = ''.join(format(ord(hz3),'b') for hz3 in z3)
# # print("Binary value of hz3 : ",bz3)

# z4 = bz3 + "".join(listnew[3])
# # print("Z4 = ",z4)
# decimal_representation = int(z4, 2)
# hexadecimal_string = hex(decimal_representation)
# print("\n\n\nThe hex value of Z4 = ",hexadecimal_string)

