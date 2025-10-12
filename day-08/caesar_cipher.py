from alphabet import alphabet

run = True

def caesar(direction, text, shift):
    result = ""
    for letter in text:
        if letter not in alphabet:
            result += letter
        else:
            if direction == "encode":
                alphabet_position = alphabet.index(letter) + shift
            if direction == "decode":
                alphabet_position = alphabet.index(letter) - shift
        alphabet_position %= len(alphabet)
        result += alphabet[alphabet_position]
    print(f"Here is the {direction}d result:\n{result}")

while run == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    another_word = input("Do you wish do proceed with another word? Type 'Y' to continue or 'N' to exit:\n").lower()

    if another_word == "n":
        run = False
        print("Bye.")