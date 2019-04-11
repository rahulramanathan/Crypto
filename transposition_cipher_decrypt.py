def decrypt(message,key):
    cipher_matrix = ['']*key
    for i in range(len(message)):
        cipher_matrix[i%key] += message[i]
    return "".join(cipher_matrix)
message = "SSTUSOCFRCASEC"
key = 5
print(decrypt(message,(len(message)//key)+1))