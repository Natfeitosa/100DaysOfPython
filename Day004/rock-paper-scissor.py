import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock,paper,scissors]

player=int(input("Please choose?\n0-rock\n1-paper\n2-scissor"))

cpu=random.randint(0,2)
print(game[player]+"vs CPU:\n" + game[cpu])

if(player==cpu):
    print("Game is a draw")
elif((player==0 and cpu==1) or (player==1 and cpu==2) or (player==2 and cpu==0)):
    print("You lose")
else:
    print("YOU WIN!")
