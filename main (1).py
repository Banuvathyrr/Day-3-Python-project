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

print('You are at cross road. Where do you want to go? Type "Left" or "Right"')
left_or_right = input()
lower_lr = left_or_right.lower()

if lower_lr == "left":
  print("You come to a lake. There is an island in the middle of the lake.Type 'wait' to wait for a boat. Type 'swim' to swim across.")
  wait_or_swim = input()
  lower_wos = wait_or_swim.lower()
  if lower_wos == "wait":
    print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
    red_or_yellow_or_blue = input()
    lower_royob = red_or_yellow_or_blue.lower()
    if lower_royob == "yellow":
        print("You win!")
    elif lower_royob == "red" or lower_royob == "blue":
        print("Game over!")
  else :
    print("Game over!")
else :
  print("Game over!")