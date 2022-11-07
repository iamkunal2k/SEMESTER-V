# Experiment - 6
# RSA ALGORITHM AND DIGITAL SIGNATURE SCHEME

print("-------------RSA ENCRYPTION/DECRYPTION-------------------")

# Input Prime Numbers
print("PLEASE ENTER THE 'p' AND 'q' VALUES BELOW:")
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))
print("---------------------------------------------------------")

# Check if Input's are Prime


def prime_check(a):
    if(a == 2):
        return True
    elif((a < 2) or ((a % 2) == 0)):
        return False
    elif(a > 2):
        for i in range(2, a):
            if not(a % i):
                return False
    return True


check_p = prime_check(p)
check_q = prime_check(q)
while(((check_p == False) or (check_q == False))):
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    check_p = prime_check(p)
    check_q = prime_check(q)

# Calculating RSA MODULES

n = p * q
print("RSA Modulus(n) is:", n)

fn = (p-1)*(q-1)
print("fn = ", fn)


# GCD

def egcd(e, fn):
    while(fn != 0):
        e, fn = fn, e % fn
    return e

# Euclid's Algorithm


def eugcd(e, fn):
    for i in range(1, fn):
        while(e != 0):
            a, b = fn//e, fn % e
            if(b != 0):
                print("%d = %d*(%d) + %d" % (fn, a, e, b))
            fn = e
            e = b

# Extended Euclidean Algorithm


def eea(a, b):
    if(a % b == 0):
        return(b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)" % (gcd, a, t, s, b))
        return(gcd, t, s)

# Multiplicative Inverse


def mult_inv(e, fn):
    gcd, s, _ = eea(e, fn)
    if(gcd != 1):
        return None
    else:
        if(s < 0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d." %
                  (s, s, s % fn))
        elif(s > 0):
            print("s=%d." % (s))
        return s % fn


# e Value Calculation
'''FINDS THE HIGHEST POSSIBLE VALUE OF 'e' BETWEEN 1 and fn THAT MAKES (e,r) COPRIME.'''
for i in range(2, fn):
    if(egcd(i, fn) == 1):
        e = i
        break
print("The value of e is:", e)
print("------------------------------------------------------")

# d, Private and Public Keys

print("EUCLID'S ALGORITHM : ")
eugcd(e, fn)
print("------------------------------------------------------")
print("EUCLID'S EXTENDED ALGORITHM : ")
d = mult_inv(e, fn)
print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'.")
print("The value of d is:", d)
print("------------------------------------------------------")
public = (e, n)
private = (d, n)
print("Private Key is :", private)
print("Public Key is :", public)

print("-------------------------------------------------------")
print("------------------DIGITAL SIGNATURE--------------------")

m = int(input("Enter the msg sent by Alice : "))

ss = (m**d) % n
print("The Signature created is  : ", ss)


m1 = (ss**e) % n

if m == m1:
    print("Accept the msg send by the Alice")
else:
    print("Do not accept the msg send by the Alice, since it is not same")

print("---------------------------------------------------------")
print("----------------------IN CRYPTOSYSTEM--------------------")
c = m**e % n
print("The encrypted msg is : ", c)
d = m**d % n
print("The Decrypted msg is : ", d)
print("---------------------------------------------------------")

