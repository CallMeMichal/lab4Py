def caesar_cipher(message, key,alphabet=None):

    if alphabet is None:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted=""
    for letter in message:
        if ord(letter) + key > ord('z'):
            encrypted += chr(ord(letter) + key-26)
        else:
            encrypted += chr(ord(letter) + key)
        #ord zwraca kod ascii z litery
    return  str(encrypted);


print(caesar_cipher("razraz",4))

