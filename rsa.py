import math

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
phi = (p-1)*(q-1)

e = 0
for i in range(2,phi-1):
    if math.gcd(i,phi) == 1:
        e = i
        break

d = 0
for i in range(2,phi-1):
    if (e*i) % phi == 1:
        d = i
        break

print("Public Key is (",n,",",e,")",sep="")
print("Private Key is (",n,",",d,")",sep="")

# encryption
plain_msg1 = [15,20,17,20]
cipher_msg1 = []

for i in plain_msg1:
    cipher_msg1.append(pow(i,e)%n)
print(cipher_msg1)

# decryption
cipher_msg2 = [9,14,29,14]
plain_msg2 = []

for i in cipher_msg2:
    plain_msg2.append(pow(i,d)%n)
print(plain_msg2)






               
