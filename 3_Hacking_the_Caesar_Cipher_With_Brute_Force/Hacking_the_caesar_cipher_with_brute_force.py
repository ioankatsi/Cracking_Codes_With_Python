# Caesar Cipher with Brute Force
# https://www.nostarch.com/crackingcode/ (BSD Licensed)

print('----------------------------------------------\n')
print('|      Caesar Cipher  With Brute-Force        |\n')
print('----------------------------------------------\n')

#The encryption/decryption key:
messageInput = 'Please enter the message to be decrypted :\n'
message = raw_input(messageInput)

# Every possible that can me encrypted :
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Loop through every possible key:
for key in range(len(SYMBOLS)):
    # It is important to set translated to the blank string so thta the
    # previous iteration's value for translated is cleared
    translated = ''
    # Loop through each symbol in message:
    for symbol in message :
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wraparound:
            if translatedIndex < 0 :
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]

        else:
            # Append the symbol without encrypting/decrypting
            translated = translated + symbol

    # Display every possible decryption:
    print('Key #%s: %s' % (key, translated))
