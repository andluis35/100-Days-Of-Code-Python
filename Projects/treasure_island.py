print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("\n-------------------------------------------------\n")
print("You're at a cross road. Where do you want to go?")

choice = input("    Type 'left' or 'right': ").lower()
print("\n-------------------------------------------------\n")

if choice == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice = input("    Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    print("\n-------------------------------------------------\n")

    if choice == "wait":
        print("A boat arrives and takes you to the Conundrum House. At the entrance, there's three doors.")
        choice = input("    Type the door you choose:\n[R] Red\n[B] Blue\n[Y] Yellow\n").lower()
        print("\n-------------------------------------------------\n")

        if choice == "r" or choice == "b":
            print("HA! A clown comes out screaming. You've had a heart attack. GAME OVER!")
        elif choice == "y":
            print("The door reveals the secret treasure. YOU'VE WON!!!")
        else:
            print("Restart the game and choose a valid door.")

    elif choice == "swim":
        print("FOOL! You remembered you didn't know how to swim. You drowned. GAME OVER!")
    else:
        print("Restart the game and choose a valid action.")

elif choice == "right":
    print("Oh no. You've crossed with a huge monster. It kills you. GAME OVER!")
else:
    print("Restart the game and choose a valid direction.")
