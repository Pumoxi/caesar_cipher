
[Link to my Blogpost](https://pumoxi.com/2024/11/11/caesar-cipher-encrypting-and-decrypting-text-with-python/)


# Caesar Cipher Encryption & Decryption Tool

A simple Python program that uses the Caesar Cipher technique to encrypt and decrypt messages by shifting letters in the alphabet.

## How It Works

This program lets users encode or decode messages with a Caesar Cipher, which shifts each letter in the message by a specified number of positions in the alphabet.

- **Encrypt**: Moves each letter in the text forward by the specified shift value.
- **Decrypt**: Reverses the shift to retrieve the original text.
- **Preserves Spaces**: Spaces and other non-alphabet characters remain unchanged.

## Example Usage

1. **Clone the repository**:
    ```bash
    git clone git@github.com:Pumoxi/caesar_cipher.git
    cd caesar-cipher-tool
    ```

2. **Run the program**:
    ```bash
    python caesar_cipher.py
    ```

3. **Encryption Example**:
    - Text: `"hello world"`
    - Shift: `3`
    - Output: `"khoor zruog"`

4. **Decryption Example**:
    - Text: `"khoor zruog"`
    - Shift: `3`
    - Output: `"hello world"`

## Code Overview

```python
# List of a-z letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(user_input, shift):
    # Encrypts the user input by shifting letters
    # ...

def decrypt(user_input, shift):
    # Decrypts the user input by reversing the shift
    # ...

# User input and main program flow
choice = input("Do you want to encrypt or decrypt? (encode/decode)")
# ...