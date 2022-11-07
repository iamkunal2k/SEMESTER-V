import string
import numpy as np

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

    for i in text:
        if i == " ":
            encoded += "*"

        else:
            pos = alphabets.index(i)
            if pos < 25:
                encoded += alphabets[(pos + key) % 26]

            else:
                encoded += alphabets[(pos + key) % len(alphabets)]
    return encoded


def transposition(text, key):
    c = key
    A = []
    B = []

    for char in text:
        A.append(char)

    matrix = list(seperate_list(A, key))

    r = len(matrix)

    print(matrix)

    transpose = np.transpose(matrix)
    transposematrix = [list(item) for item in transpose]
    print(transposematrix)

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
    return encrypt


plain_text = input("Enter the Text to encode : ")
substitute_key = int(input("Enter the shift key : "))
substitute_cipher = subs(plain_text, substitute_key)
print("subs cipher : ", substitute_cipher)
print('------------------------------------------')
transpose_key = int(input("Enter the tranpose key: "))
encrypt = transposition(substitute_cipher, transpose_key)
print("Product Cipher : ", encrypt)


# print("======================DECRYPTION===============================")

# def decode(encrypt, key) :
#     c = key
#     A = []
#     B = []

#     for char in encrypt:
#         A.append(char)

#     matrix = list(seperate_list(A, key))

#     r = len(matrix)

#     print(matrix)
    
# decode(encrypt, transpose_key)

    # transpose = np.transpose(matrix)
    # transposematrix = [list(item) for item in transpose]
    # print(transposematrix)
    
    # print("------------------------------------------------")
    #     for i in range(r):
    #         for j in range(c):
    #             print(matrix[i][j], end=" ")
    #         print()

    #     print("-------------------------------------------------")
    #     for j in range(c):
    #         for i in range(r):
    #             if matrix[i][j] is not None:
    #                 B.append(matrix[i][j])
    #     encrypt = "".join(B)
    #     return decrypt



# # DECRYTION

# # Defining Old character of each character

# for i in range(len(alphabets)):        # 26
#     old_character[alphabets[i]] = alphabets[(i - key) % len(alphabets)]


# for char in encrypt:
#     if char in alphabets :
#         temp = old_character[char]
#         decoded.append(temp)

#     else :
#         temp = char
#         decoded.append(temp)


# # Joining the values which is stored in the list in the form of string
# decrypt = "".join(decoded)

# print("Decypted message is : ", decrypt)
