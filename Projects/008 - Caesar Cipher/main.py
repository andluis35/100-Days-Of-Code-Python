import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    encoded_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        encoded_text += alphabet[shifted_position]

    print("******************************************")
    print(f"Here is the encoded result: {encoded_text}")
    print("******************************************")

def decrypt(original_text, shift_amount):
    decoded_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        decoded_text += alphabet[shifted_position]

    print("******************************************")
    print(f"Here is the decoded result: {decoded_text}")
    print("******************************************")

def caesar():
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("You've typed an invalid operation. Restart the program and try again.")


should_continue = True

while should_continue:
    print("-----------------------------------------------------------------")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    print("-----------------------------------------------------------------")
    text = input("Type your message:\n").lower()
    print("-----------------------------------------------------------------")
    shift = int(input("Type the shift number:\n"))
    print("-----------------------------------------------------------------")

    caesar()

    choice = int(input("Do you want to continue?\n[1] Yes\n[2] No\nR: "))
    if choice != 1:
        should_continue = False
        print("\n=-=-=-=-=-=-=-=-=-=-=")
        print("Finishing program....")
        print("=-=-=-=-=-=-=-=-=-=-=")
