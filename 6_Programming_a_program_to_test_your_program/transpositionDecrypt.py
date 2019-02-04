# Transposition Cipher Decryption
# https://www.nostarch.com/crackingcode/ (BSD Licensed)

import math

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)

    # Print with | (called "pipe" character ) after it in case
    # there are spaces at the end of the decrypted message :
    print(plaintext + '|')

def decryptMessage(key, message):
    # The Transposition decrypt function will simulate the columns
    # and rows of the grid that the plaintext is written on by using a list
    # of string. FIrst, we need to calculate a few values.

    # The number of columns in our Transposition grid:
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # The number of rows in our grid :
    numOfRows = key
    # The number of 'shaded boxes' in the last 'column' of the grid :
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid :
    plaintext = [''] * numOfColumns

    # The column and row variable points to where in the grid the next
    # character in the encrypted message will go :
    column = 0
    row = 0

    for symbol in message :
        plaintext[column] += symbol
        column += 1 # Point to the next column

        # if there are no more columns OR we are at the shaded box, go back
        # to the first column and the next row :
        if (column == numOfColumns) or (column == numOfColumns - 1 and
            row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)

# if transpositionDecrypt.py is run (insted of imported as a module),
# call the main() function:
if __name__ == '__main__':
    main()
