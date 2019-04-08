LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encr_decr(text, key, mode):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]

        if mode is "E":
            # Encrypt uppercase characters in plain text
            if char in LETTERS:
                result = result + chr((ord(char) + key - 65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                result = result + char
        elif mode is "D":
            # Decrypt uppercase characters in plain text
            if char in LETTERS:
                result = result + chr((ord(char) - key - 65) % 26 + 65)
            # Decrypt lowercase characters in plain text
            else:
                result = result + char
        else:
            result = "Invalid Mode"
    return result

# check the above function
text = "WYGGIWWJEGXSVW".upper()
key = 4

print("Plain Text : " + text)
print("Shift pattern : " + str(key))
print("Cipher: " + encr_decr(text, key, "D"))
