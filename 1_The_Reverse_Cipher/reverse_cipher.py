#Reverse Cipher

message = raw_input('Enter message to be encrypted:\n')
translated = ''

i = len(message) - 1
while i >= 0 :
  translated = translated + message[i]
  i -= 1

print(translated)
