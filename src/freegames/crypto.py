"""Crypto: tool for encrypting and decrypting messages.

Exercises

1. Review 'ord' and 'chr' functions and letter-to-number mapping.
2. Explain what happens if you use key 26.
3. Find a way to decode a message without a key.
4. Encrypt numbers.
5. Make the encryption harder to decode.

Adapted from code in https://inventwithpython.com/chapter14.html
"""

def shift_char(char, shift):
    if char.isalpha():
        is_upper = char.isupper()
        base = ord('A') if is_upper else ord('a')
        shifted_char = chr(((ord(char) - base + shift) % 26) + base)
        return shifted_char
    elif char.isdigit():
        # Encrypt digits as well
        return str((int(char) + shift) % 10)
    else:
        return char

def encrypt(message, key):
    """Encrypt message with key."""
    result = ''.join([shift_char(char, key) for char in message])
    return result

def decrypt(message, key):
    """Decrypt message with key."""
    return encrypt(message, -key)

def decode(message):
    """Decode message without key."""
    for key in range(26):
        decrypted_message = decrypt(message, key)
        print(f"Key {key}: {decrypted_message}")

def get_key():
    """Get key from user."""
    while True:
        try:
            key = int(input('Enter a key (1 - 25): '))
            if 1 <= key <= 25:
                return key
            else:
                print('Invalid key. Key must be between 1 and 25.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

print('Do you wish to encrypt, decrypt, or decode a message?')
choice = input().lower()

if choice == 'encrypt':
    phrase = input('Message: ')
    code = get_key()
    print('Encrypted message:', encrypt(phrase, code))
elif choice == 'decrypt':
    phrase = input('Message: ')
    code = get_key()
    print('Decrypted message:', decrypt(phrase, code))
elif choice == 'decode':
    phrase = input('Message: ')
    print('Decoding message:')
    decode(phrase)
else:
    print('Error: Unrecognized Command')

