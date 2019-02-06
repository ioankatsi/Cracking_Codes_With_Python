# Transposition Cipher
# https://www.nostarch.com/crackingcode/ (BSD Licensed)

def main():
    messageInput = 'Please enter the message to be encrypted :\n'
    myMessage = input(messageInput)
    myKey = 3

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe character") after it in case there are spaces at
    # the end of the encrypted message:
    print(ciphertext + '|')


def encryptMessage(key, message):
    # Each string in ciphretext represents a column in the grid:
    ciphertext = ['']*key

    # Loop through each column in ciphertext :
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length:
        while currentIndex < len(message):
            # Place the character at the currentIndex in message at the
            # end of the current column in the ciphertext list :
            ciphertext[column] += message[currentIndex]

            # Move currentIndex over :
            currentIndex += key

    # Convert the ciphertext list into a single string value and return it:
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
