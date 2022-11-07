def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("".join(key))
   
def encryption(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("".join(cipher_text))

def decryption(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("".join(orig_text))

string = str(input("Plaintext: "))
string = string.upper()
keyword = str(input("Key: "))
keyword = keyword.upper()
key = generateKey(string, keyword)
cipher_text = encryption(string,key)
print("Ciphertext :", cipher_text)
print("Decrypted Text :", decryption(cipher_text, key))
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("".join(key))
   
def encryption(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("".join(cipher_text))

def decryption(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("".join(orig_text))

string = str(input("Enter Plaintext: "))
string = string.upper()
keyword = str(input("Enter Key: "))
keyword = keyword.upper()
key = generateKey(string, keyword)
cipher_text = encryption(string,key)
print("Ciphertext :", cipher_text)
print("Decrypted Text :", decryption(cipher_text, key))

