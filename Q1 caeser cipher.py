def get_plain_text():
    plain_text = input("Enter the plain text for Encryption:")
    return plain_text

def get_offset():
    offset = int(input("Enter offset: "))
    return offset

def caesar_cipher(plain_text, offset):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_text = []

    if offset < 0:
        shifted_letters = letters[abs(offset):] + letters[: abs(offset)]
    elif offset > 0:
        shifted_letters = letters[-offset:] + letters[:-offset]
    else:
        shifted_letters = letters

    letters = letters + letters.lower()
    shifted_letters = shifted_letters + shifted_letters.lower()
        
    for text in plain_text:
        if text.isalpha():
            for i in range(52):
                if text == letters[i]:
                    cipher_text.append(shifted_letters[i])
        else:
            cipher_text.append(text)

    for item in cipher_text:
        print(item, end="")

    return cipher_text

# function call
caesar_cipher(get_plain_text(), get_offset())


