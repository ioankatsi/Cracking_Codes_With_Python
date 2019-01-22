# Cracking Codes With Python
### These chapters are from Cracking Codes With Python Book written from Al Sweigart. <br>Every Chapter, generally alternate between a Cipher and how You can hack that cipher. <br>The Book can be found [Here](https://nostarch.com/crackingcodes).

# Brief Contents
- The Reverse Cipher
- The Caesar Cipher
- Hacking the Caesar Cipher with Brute-Force
- Encrypting with Transposition Cipher
- Decrypting with the Transposition Cipher
- Programming a Program to Test Your Program
- Encrypting and Decrypting Files
- Detecting English Programmatically
- Hacking the transposition Cipher
- A Modular Arithmetic Module for the Afiine Cipher
- Programming the Affine Cipher
- Hacking The Afiine Cipher
- Programming the Simple Substitution Cipher
- Hacking the Simple Substitution Cipher
- Programming the Vigenére Cipher
- Frequency Analysis
- Hacking the Vigenére Cipher
- The One-Time Pad Cipher
- Finding and Generating Prime Numbers
- Generating Keys for the Public Key Cipher
- Programming the Public Key Cipher

1) ### The Reverse Cipher
The reiverse cipher encrypts a message by printing it in reverse order. So "Hello, world!" encrypts to "!dlrow , olleH". To Decrypt, or ger the original message, you simpy reverse the encrypted message. The encryption and the decryption steps are the same .

2) ### The Caesar Cipher
The reverse cipher encrypts the same way. But the Ceaser cipher uses keys, which encrypt the message differently depending on which key is used. The keys for the Caesar cipher are the integers from 0 to 25. Even if a cryptanalyst knows the Caesar cipher was used, that alone doesn't give them enough information to break the cipher. The must also know the key.

3) ### Hacking The Caesar Cipher With Brute-Force
We can hack the Caesar cipher by using a cryptanalytic technique called brute-force. A brute-force attack tries every possible decryption key for a cipher.
