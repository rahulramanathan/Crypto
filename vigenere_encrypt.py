LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encrypt(text, key):
    result = ""

    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        rep = len(text)//len(key) + 1
        # Encrypt uppercase characters in plain text
        key *= rep

        if (char in LETTERS):
            result = result + chr((ord(char) + ord(key[i]) - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result = result + char
    return result

# check the above function
text = "SUCCESSFACTORS".upper()
key  = "RAHUL"

print("Plain Text : " + text)
print("Key : " + str(key))
print("Cipher: " + encrypt(text, key))