print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
decision1=input("The road splits into two, you must choose to go left or right?")
if(decision1=='left'):
    print("You went left, while on the road you activated a pitfall trap and perished!")
    print("GAME OVER")
else:
    print("going right, you found a map with the location of the treasure. The map leads you to a castle")
    print("while in the castle the treasure is behind one of the 3 doors you encounter.")
    print("The doors are numbered 1,2,3, and 4")
    door=int(input("which door do you choose?"))
    if(door==1):
        print("Behind that door you find a beast that instantly kills you")
        print("GAME OVER")
    elif(door==2):
        print("When the door opens, a trap is trigger causing an explosion")
        print("GAME OVER")
    elif(door==3):
        print("Once the door opens you are rushed by a cloud of poisonous gases")
        print("GAME OVER")

    else:
        print("When you open the door you find the treasure and all the riches, congratulations you win!")
        print("VICTORY!")
