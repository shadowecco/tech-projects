#Python functions

import random
import time

#User-created functions

from ranks import *

#User created functions

from invalid_choices import *

ts750ms = 750/1000 #750 milliseconds
ts1s = 1 #1 second

health = 10

#Selects a random name for the player if they select a name to be randomly selected.

def random_name(ans):
    if ans == "m":
        file = open('male_names.txt', 'r')
    elif ans == "f":
        file = open('female_names.txt', 'r')
    name = (random.choice(file.read().splitlines()))
    return name
    file.close()


#Selects the "Welcome to Ravenbrooke" in accordance to the rank they chose.

def welcome_sentence(name, rank):
    if rank == "Lord" or rank == "Lady":
        welcomeSentence = ("Welcome to the mythical kingdom of Ravenbrooke " + rank + " " + name + ".")
        return (welcomeSentence)
    elif rank == "Witch" or rank == "Wizard" or rank == "Knight":
        welcomeSentence = ("Welcome to the mythical kingdom of Ravenbrooke " + name + ", young " + rank + " in training.\n"
                        "Let's put your training to the test, young student.")
        return (welcomeSentence)
    else:
        welcomeSentence = ("Welcome to the mythical kingdom of Ravenbrooke " + name + ", brave and noble " + rank + ".\n"
                        "Let's prove your worth to the kingdom.")
        return (welcomeSentence)

#Selects the start of story in accordance to the rank they chose. 

def start_sentence(rank):

    if rank == "Witch" or rank == "Wizard" or rank == "Wizard":
        startSentence = ("A spell went wrong and POOF! You find yourself in a house far way from your home.\n"
                         "After a few seconds of panic, you waved your wand to try to get yourself back but \n"
                         "it fizzles and dies. Your wand is broken and you are trapped.  ")
        return (startSentence)
    else:
        startSentence = ("You were minding your own business when suddenly POOF! You find yourself in a house far way "
                         "from your home.")
        return (startSentence)