# list of a to z

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt (user_input, shift):
    encrypted = ""
    for i in user_input:
        if i == " ":
            encrypted += " "
        else:
            index = alphabet.index(i)
            encrypted += alphabet[(index + shift) % 26]
    return encrypted

def decrypt (user_input, shift):
    decrypted = ""
    for i in user_input:
        if i == " ":
            decrypted += " "
        else:
            index = alphabet.index(i)
            decrypted += alphabet[(index - shift) % 26]
    return decrypted

def main():

    choice = input("Do you want to encrypt or decrypt? (encode/decode)")

    if choice == "encode":
        user_input = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value: "))
        print(encrypt(user_input, shift))
    else:
        user_input = input("Enter the text to decrypt: ")
        shift = int(input("Enter the shift value: "))
        print(decrypt(user_input, shift))

if __name__ == "__main__":
    main()