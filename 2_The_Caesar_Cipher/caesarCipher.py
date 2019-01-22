# Caesar Cipher
# Basic example from https://www.nostarch.com/crackingcodes/  (BSD Licensed)
import paperclip

print('-------------------------\n')
print('|     Caesar Cipher     |\n')
print('-------------------------\n')
print('Hello, What would you like to do? :')
print('1. Encrypt with Caesar Cipher')
print('2. Decrypt with Caesar Cipher')
status = raw_input()

# Whether the program encrypts or decrypts :
if status == '1' or status == 'encrypt':
    mode = 'encrypt'
elif status == '2' or status == 'decrypt':
    mode = 'decrypt'

#The encryption/decryption key:
keyMessage = 'Please enter the key to ' + mode +' :\n'
key = int(raw_input(keyMessage))

#The encryption/decryption message:
messageInput = 'Enter message to be ' + mode +'ed:\n'
message = raw_input(messageInput)

# Every possible that can me encrypted :
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store the encrypted /decrypted form of the message :
translated = ''

for symbol in message :
    # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform encryption/decryption :
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handle wraparound, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

# Output the translated string:
print(translated)
paperclip.copy(translated)
