def encrypt(message,key):
    cipher_matrix = ['']*key
    for i in range(len(message)):
        cipher_matrix[i%key] += message[i]
    return "".join(cipher_matrix)
message = "SUCCESSFACTORS"
key = 5
print(encrypt(message,key))