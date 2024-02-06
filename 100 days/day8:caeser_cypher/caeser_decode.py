alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]



enc = []

def encrypt(text, shift):
    for letter in text:
        pos = alphabet.index(letter)
        new_pos = pos + shift
        if new_pos < 25:
            enc.append(alphabet[new_pos])
        else:
            enc.append(alphabet[new_pos - 26])


    print(f"The encoded text is {' '.join(enc)}")
    return enc

def decrypt(enc, shift):
    dec = []
    for letter in enc:
        pos = alphabet.index(letter)
        new_pos = pos - shift
        #print(new_pos)
        if new_pos < 1:
            dec.append(alphabet[26 + new_pos])
        else:
            dec.append(alphabet[pos])
    print(f"The decoded text is {' '.join(dec)}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#e.g.
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

if direction =='encode' or direction =='decode':
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

else:
  print('Enter a valid choice please.')

if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(enc, shift)



