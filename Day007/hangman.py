import random

#Step 1

word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']




gameover= False
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word=random.choice(word_list)
#This is meant to test the code
print("The word is: "+ word)
display=[]
for i in range(0,len(word)):
    display.append("_")
lives=0
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while(not gameover):
    print(stages[lives])
    player_choice=input("Pick a letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    in_display=False
    for i in range(0,len(word)):
        if word[i]==player_choice:
            display[i]=player_choice
            in_display=True
        
    if "_" not in display:
        print("You solved the word!")
        gameover=True
    print(display)
    if not in_display:
        print("Letter is not in the word")
        lives+=1
    if lives==(len(stages)-1):
        gameover=True
        print("Couldnt solve the word, GAME OVER")
        
        

