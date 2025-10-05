from alphabet import alphabet

# direction = input("Type 'encode to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    result = ""
    for letter in text:
        alphabet_position = alphabet.index(letter) + shift
        result += alphabet[alphabet_position]

    print(result)

encrypt("asdasdasd", 3)