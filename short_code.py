# Subsitution Cipher

ALPHABATES = list(map(chr, range(ord('a'), ord('z')+1))) + \
    list(map(chr, range(ord('A'), ord('Z')+1)))


def EncodeShort(text, key=4):
    return "".join([ALPHABATES[(ALPHABATES.index(i)+key) % len(ALPHABATES)] if i != " " else "$" for i in text])


def DecodeShort(text, key=4):
    return "".join([ALPHABATES[(ALPHABATES.index(i)-key) % len(ALPHABATES)] if i != "$" else " " for i in text])


text = "good morning"
encoded = EncodeShort(text)
print("Encoded ", encoded)
decoded = DecodeShort(encoded)
print("Decoded ", decoded)


# Transposition Cipher

def makeMatrixShort(text, size=5):
    t1 = [list(text[i:i+size]) for i in range(0, len(text), size)]
    # fill the last row with empty strings
    t1[-1] += ['']*(size-len(t1[-1]))
    return t1


def encode(text):
    mat = makeMatrixShort(text)
    return "".join([mat[j][i] for i in range(len(mat[0])) for j in range(len(mat))])


print(encode("WEAREDISCOVERED"))

# vigenere Cipher
ALPHABATES = list(map(chr, range(ord('A'), ord('Z')+1)))


def encryptShort(text, key="HEALTH"):
    return "".join([ALPHABATES[(ALPHABATES.index(text[i])+ALPHABATES.index(key[i % len(key)])) % len(ALPHABATES)] for i in range(len(text))])


print(encryptShort("LIFEISFULLOFSURPRISES"))


# Frequency analysis :

# initializing string
total = str(decrypt)

# using naive method to get count
# of each element in string
all_freq = {}

for i in total:
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
