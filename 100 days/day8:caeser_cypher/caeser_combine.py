import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shift = shift %26

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caeser(text,shift,direction):
    new_text = ""
    new_pos= 0
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == "encode":
                new_pos = position + shift
                new_text+=alphabet[new_pos]
            
            elif direction =="decode":
                new_pos = position - shift
                new_text+=alphabet[new_pos]
        else:
            new_text+=char
    print(f"The {direction}d is {new_text}")
 

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caeser(text,shift,direction)