from enigma import encode_enigma, decode_enigma, generate_random_code, format_string
from utils import split_words
choice = int(input('\nWould you like to 1: Encode or 2: Decode? Please type in the corresponding number: '))
if choice == 1:
    choice = input('\nDo you have a code? If not one will be generated. (y)es/(n)o: ').lower()
    if choice == 'n':
        code = generate_random_code()
        print('\nCode:', code)
        print('\nMake sure to save it\n')
    else:
        code = input('Please type in your code: ')
    msg = input('What is the message you would like to encode? ')
    msg = format_string(msg)
    print('\nFormatted Message:\n' +  msg)
    print('\nHere is the encoded message:')
    print(encode_enigma(msg, code))
else:
    code = input('\nPlease type in your code: ')
    msg = input('\nPlease type in your encoded message: ')
    print('\nHere is your decrypted message:')
    decoded = decode_enigma(msg, code)
    print(decoded)
    print('\nHere is an attempt to split it up into words:')
    print(split_words(decoded))