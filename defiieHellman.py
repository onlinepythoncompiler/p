import math

def isPrime(num):
    for i in range(2,num-1):
        if (num%i) == 0:
            return False
    return True

p = int(input("Enter the value of p: "))
while(isPrime(p) == False):
    p = int(input("p needs to be prime! Enter again: "))
    
g = int(input("Enter the value of g: "))
while(isPrime(g) == False):
    g = int(input("g needs to be prime! Enter again: "))

a = int(input("Enter a: "))
b = int(input("Enter b: "))

aliceSent = pow(g,a) % p
bobSent = pow(g,b) % p
print("Alice sent",aliceSent)
print("Bob sent",bobSent)

aliceKey = pow(bobSent,a) % p
bobKey = pow(aliceSent,b) % p
print("Shared key of Alice is",aliceKey)
print("Shared key of Bob is",bobKey)
