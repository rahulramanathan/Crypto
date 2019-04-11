def encr_decr(message,key,mode):
    if mode is 'E':
        pass
    elif mode is 'D':
        key = len(message) // key + 1
    else:
        return 'Invalid Mode'
    cipher_matrix = ['']*key
    for i in range(len(message)):
        cipher_matrix[i%key] += message[i]
    return "".join(cipher_matrix)

message = "SSTUSOCFRCASEC"
key = 5
mode = 'D'
print(encr_decr(message,key,mode))