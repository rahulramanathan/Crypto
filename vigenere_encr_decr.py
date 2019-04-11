LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(text, key, mode):
    result = ""

    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        rep = len(text)//len(key) + 1
        # Encrypt uppercase characters in plain text
        key *= rep

        if mode is 'E':
            if char in LETTERS:
                result = result + chr((ord(char) + ord(key[i]) - 65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                result = result + char
        elif mode is 'D':
            if char in LETTERS:
                result = result + chr((ord(char) - ord(key[i]) - 65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                result = result + char
        else:
            result = 'Invalid mode'
    return result


# check the above function
text = "WHWJCWFZHAXBLZ".upper()
key = "RAHUL"
mode = 'E'
print("Plain Text : " + text)
print("Key : " + str(key))
print("Result: " + encrypt(text, key, mode))
