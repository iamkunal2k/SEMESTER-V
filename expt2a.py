#PRODUCT CIPHER USING SUBSTITUTION CIPHER

import string

alphabets = string.ascii_letters


def seperate_list(list1, n):
    for i in range(0, len(list1), n):
        each_character = list1[i: n+i]

        if len(each_character) < n:
            each_character = each_character + \
                [None for y in range(n-len(each_character))]
        yield each_character


def subs(text, key):
    encoded = ""
    list3 = []
    for i in text:
        if i == " ":
            encoded += "*"

        else:
            pos = alphabets.index(i)
            if pos < 25:
                encoded += alphabets[(pos + key) % 26]

            else:
                encoded += alphabets[(pos + key) % len(alphabets)]

    for i in encoded:
        if i is None:
            list3.append("$")
        else:
            list3.append(i)
    return encoded


def transposition(text, key):
    c = key
    A = []
    B = []

    for char in text:
        A.append(char)

    matrix = list(seperate_list(A, key))
    matrix1 = matrix

    r = len(matrix)
    # print(r)
    print(matrix)

    print("------------------------------------------------")
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end=" ")
        print()

    print("-------------------------------------------------")
    for j in range(c):
        for i in range(r):
            if matrix[i][j] is not None:
                B.append(matrix[i][j])
    encrypt = "".join(B)
    return encrypt, matrix


plain_text = input("Enter the Text to encode : ")
substitute_key = int(input("Enter the shift key : "))
substitute_cipher = subs(plain_text, substitute_key)
print("subs cipher : ", substitute_cipher)
print('------------------------------------------')
transpose_key = int(input("Enter the tranpose key: "))
encrypt, matrix = transposition(substitute_cipher, transpose_key)
print("Product Cipher : ", encrypt)


def decrypt(matrix):
    list_decrypt = []
    r = len(matrix)
    c = transpose_key
    for i in range(r):
        for j in range(c):
            list_decrypt.append(matrix[i][j])
    print(list_decrypt)

    list3 = []
    for i in list_decrypt:
        if i is None:
            list3.append("")
        else:
            list3.append(i)

    print(list3)

    decrypt_text = "".join(list3)

    decdict = {}
    for j in range(len(alphabets)):
        decdict[alphabets[j]] = alphabets[(j-substitute_key) % len(alphabets)]

    decrypt = []

    for d in decrypt_text:
        if d in alphabets:
            decrypt.append(decdict[d])
        else:
            decrypt.append(" ")

    dectext = "".join(decrypt)
    print("Decypted Text: ", dectext)


print("--------------------------------------------\n")
print("===============Decrpytion===================\n")
decrypt(matrix)
