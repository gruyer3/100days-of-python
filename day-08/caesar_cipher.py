from alphabet import alphabet

#direction = input("Type 'encode to encrypt, type 'decode' to decrypt:\n").lower()
#text = input("Type your message:\n").lower()
#shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    result = ""
    for letter in text:
        alphabet_position = alphabet.index(letter) + shift
        alphabet_position %= len(alphabet)
        result += alphabet[alphabet_position]
    print(result)

def decrypt(text, shift):
    result = ""
    for letter in text:
        alphabet_position = alphabet.index(letter) - shift
        alphabet_position %= len(alphabet)
        result += alphabet[alphabet_position]
    print(result)


#encrypt("z", 3)
#decrypt("a", 24)