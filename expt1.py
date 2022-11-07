# SUBSTITUTION CIPHER

import string

alphabets = string.ascii_letters

# Input Values

message = input("Enter the message : ")
key = int(input("Enter the key value : "))

# List created
encoded = []
decoded = []

# Creating the dictionary to store the substitution of characters in message depending on the key

Shifted_character = {}
old_character = {}

# Defining new position of each character

for i in range(len(alphabets)):        # 26
    Shifted_character[alphabets[i]] = alphabets[(i + key) % len(alphabets)]

# looping through the each character that is present in the message and replacing that character with shifted character
for char in message:
    if char in alphabets :
        temp = Shifted_character[char]
        encoded.append(temp)
        
    else :
        temp = char
        encoded.append(temp)

# Joining the values which is stored in the list in the form of string
encrypt = "".join(encoded)

print("Encrypted message is : ", encrypt)


# DECRYTION

# Defining Old character of each character

for i in range(len(alphabets)):        # 26
    old_character[alphabets[i]] = alphabets[(i - key) % len(alphabets)]


for char in encrypt:
    if char in alphabets :
        temp = old_character[char]
        decoded.append(temp)
        
    else :
        temp = char
        decoded.append(temp)


# Joining the values which is stored in the list in the form of string
decrypt = "".join(decoded)

print("Decypted message is : ", decrypt)


# Frequency analysis :

# initializing string
total = str(decrypt)

# using naive method to get count
# of each element in string
all_freq = {}

for i in total :
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1


# printing result
print("Counting all characters :\n "
      + str(all_freq))


def percentage(dictionary, s):
    sum = 0
    for key in dictionary:
        sum += dictionary[key]

    return float((dictionary[s]) / float(sum)) * 100

key = str(input("Enter the character to find the percentage of it : "))
print(percentage(all_freq, key))








# frequency = {}

# str(decrypt)
# for occurance in decrypt :
#     if occurance in frequency :
#         frequency[occurance] += 1

#     else :
#         frequency = 1

# frequency = (frequency % 26) * 100

# print("Frequency of each character : " + str(frequency))
