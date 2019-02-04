# Transposition Cipher Test
# https://www.nostarch.com/crackingcodes/

import random, sys, encrypting_with_the_transposition_cipher, transpositionDecrypt

def main():
    random.seed(42) # set the random "seed " to static value.

    for i in range(20): # run 20 tests
        # Generate random messages to test.

        # The message will have a random length
        message = 'ABCDEFGHIJKLMOPQRSTUVWXYZ' * random.randint(4,40)

        # Convert the message string to a list to shuffle it :
        message = list(message)
        random.shuffle(message)
        message = ''.join(message) # Convert the list back to a string.

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        # Check all posible keys for each message :
        for key in range(1, int(len(message)/2)):
            encrypted =  encrypting_with_the_transposition_cipher.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            # If the decryption does not match the original message, display
            # an error messag and quit:
            if message != decrypted :
                print('Mismatch with key %s and message %s.' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('Transposition cipher test passed.')

# If transpositionTest.py is run (instead of imported as a module) call
# the main() function:
if __name__ == '__main__':
    main()
