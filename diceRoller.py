#Dice roll program
#Describe the purpose of this program here.

import random
import time
question = "y"

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

def roll():
    print("rolling.....")
    roll = random.randint(1,6)
    return roll
    
def show_dice(roll):
    if roll == 1:
        print(S1)
    elif roll == 2:
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll == 4:
        print(s4)
    elif roll == 5:
        print(s5)
    else:
        print(s6)

while question == "y":    #Keeps rolling until the user answers "n"
    myroll = roll()
    time.sleep(1)
    show_dice(myroll)
    question = input("Roll again? (y/n) >>> ")

