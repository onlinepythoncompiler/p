import math

# encryption
def encrypt(plain_text,n):
    m = plain_text
    c = (m*m) % n
    return c

# decryption
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd,x,y = extended_gcd(b%a,a)
        return gcd, y - (b // a) * x, x

def properBinary(num):
    numBin = bin(num)
    numBin = numBin[2:]
    if(len(numBin) % 2 != 0):
        numBin = "0" + numBin
    return numBin

def decrypt(cipher_text,p,q):
    c = cipher_text
    
    gcd,a,b = extended_gcd(p,q)

    r = math.fmod(pow(c,(p+1)/4),p)
    s = math.fmod(pow(c,(q+1)/4),q)

    x = math.fmod(abs((a*p*s + b*q*r)),n)
    y = math.fmod(abs((a*p*s - b*q*r)),n)

    m1 = properBinary(int(x))
    m2 = properBinary(int(n-x))
    m3 = properBinary(int(y))
    m4 = properBinary(int(n-y))

    len1 = int(len(m1)/2)
    len2 = int(len(m2)/2)
    len3 = int(len(m3)/2)
    len4 = int(len(m4)/2)

    if m1[:len1] == m1[len1:]:
        return x
    if m2[:len2] == m2[len2:]:
        return n-x
    if m3[:len3] == m3[len3:]:
        return y
    if m4[:len4] == m4[len4:]:
        return n-y

# main
def isPrime(num):
    for i in range(2,num-1):
        if (num%i) == 0:
            return False
    return True

p = int(input("Enter the value of p: "))
while(isPrime(p) == False):
    p = int(input("p needs to be prime! Enter again: "))
    
q = int(input("Enter the value of q: "))
while(isPrime(q) == False):
    q = int(input("q needs to be prime! Enter again: "))

n = p*q

plainMSG = int(input("Enter message to be encrypted: "))
print("Encrypted message is:",encrypt(plainMSG,n))

cipherMSG = int(input("Enter message to be decrypted: "))
print("Decrypted message is:",decrypt(cipherMSG,p,q))
