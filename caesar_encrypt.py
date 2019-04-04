LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encrypt(text, key):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text

        if (char in LETTERS):
            result = result + chr((ord(char) + key - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result = result + char
    return result

# check the above function
text = "SUCCESSFACTORS".upper()
key = 4

print("Plain Text : " + text)
print("Shift pattern : " + str(key))
print("Cipher: " + encrypt(text, key))