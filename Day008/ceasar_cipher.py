alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(word,key):
    print(word)
    newword=""
    for letter in word:
        if letter.isalpha():
            new_letter=chr((ord(letter)+key))
            if ord(new_letter)>122:
                new_letter=chr((ord(new_letter)-122)+96)
            newword+=new_letter
        else:
            newword+=letter
    print(newword)

def decrypt(word,key):
    print(word)
    new_word=""
    for letter in word:
        if letter.isalpha():
            new_letter = chr((ord(letter)-key))
            if ord(new_letter)<97:
                new_letter=chr(122-(96-ord(new_letter)))
            new_word+=new_letter
        else:
            new_word+=new_letter
    print(new_word)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = (int(input("Type the shift number:\n")))%26
if direction=="encode":
    encrypt(text,shift)
elif direction=="decode":
    decrypt(text,shift)
else:
    print("Invalid choice")
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##Bug alert: What happens if you try to encode the word 'civilization'?

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
