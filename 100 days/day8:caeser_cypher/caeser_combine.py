alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caeser(text,shift,direction):
    new_text = ""
    new_pos= 0
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_pos = position + shift
            new_text+=alphabet[new_pos]
        
        elif direction =="decode":
            new_pos = position - shift
            new_text+=alphabet[new_pos]

    print(f"The text is {new_text}")
 

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caeser(text,shift,direction)