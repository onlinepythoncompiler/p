import numpy as np

plain_text = input("Enter message to be encrypted: ").lower()
plain_text = np.array([ord(i)-97 for i in plain_text]).reshape(len(plain_text),1)

key = input("Enter key: ").lower()
key = np.array([ord(i)-97 for i in key]).reshape(len(plain_text),len(plain_text))

# encryption
cipher_text = np.mod(np.dot(key,plain_text),26)
cipher_text = "".join([chr(i+97) for j in cipher_text.tolist() for i in j])
print("Encrypted text is:",cipher_text)

# finding key inverse
det = int(np.mod(np.linalg.det(key),26))
inv_det = pow(det,-1,26)

trans_key = np.linalg.inv(key)*np.linalg.det(key)

inv_key = np.mod(np.dot(inv_det,trans_key),26)
#inv_key = inv_key.astype('int8')
print("The inverse key is:")
print(inv_key)

# decryption
cipher_text = input("Enter message to be decrypted: ").lower()
cipher_text = np.array([ord(i)-97 for i in cipher_text]).reshape(len(cipher_text),1)

plain_text = np.mod(np.dot(inv_key,cipher_text),26)
plain_text = "".join([chr(round(i)%26+97) for j in plain_text.tolist() for i in j])
print("Decrypted text is:",plain_text)

# take key as GYBNQKURP and test any 3 lettes as plain_text(like act(cipher is poh), cat(inverse is fin))
