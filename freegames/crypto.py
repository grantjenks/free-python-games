"""Crypto: tool for encrypting and decrypting messages.

Exercises

1. Review 'ord' and 'chr' functions and letter-to-number mapping.
2. Explain what happens if you use key 26.
3. Find a way to decode a message without a key.
4. Encrypt numbers.
5. Make the encryption harder to decode.

"""

def encrypt(message, key):
    result = ''

    # Iterate letters in message and encrypt each individually.

    for letter in message:
        if letter.isalpha():

            # Letters are numbered like so:
            # A, B, C - Z is 65, 66, 67 - 90
            # a, b, c - z is 97, 98, 99 - 122

            num = ord(letter)

            if letter.isupper():
                base = ord('A')
            elif letter.islower():
                base = ord('a')

            # The encryption equation:

            num = (num - base + key) % 26 + base

            result += chr(num)

        elif letter.isdigit():

            # TODO: Encrypt digits.
            result += letter

        else:
            result += letter

    return result

def decrypt(message, key):
    return encrypt(message, -key)

def decode(message):
    # TODO: Decode a message without a key.
    pass

def get_key():
    try:
        key = int(input('Enter a key (1 - 25): '))
        return key
    except:
        print('Invalid key. Using key: 0.')
        return 0

if __name__ == '__main__':
    print('Do you wish to encrypt, decrypt, or decode a message?')
    choice = input()

    if choice == 'encrypt':
        message = input('Message: ')
        key = get_key()
        print('Encrypted message:', encrypt(message, key))

    elif choice == 'decrypt':
        message = input('Message: ')
        key = get_key()
        print('Decrypted message:', decrypt(message, key))

    elif choice == 'decode':
        message = input('Message: ')
        print('Decoding message:')
        decode(message)

    else:
        print('Error: Unrecognized Command')
