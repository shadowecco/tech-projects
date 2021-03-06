#Python functions

import time

ts750ms = 750/1000 #750 milliseconds
ts1s = 1 #1 second

#User-created functions

import packages.invalid_choices

# List of playable ranks - Each choice will have an effect on how the game is played. Ranks are alphabetical order

rankList = [
"Knight",
"Lady",
"Lord",
"Squire",
"Villager",
"Witch",
"Wizard",
];

#Description of ranks if players wnats to see them

rankDesc = [
"Ah, the Knight. A brave noble soul...or are you?",
"As a noble Lady of the Royal Court, you will be unused to the wilderness so this will be a challenge. Can you prove you "
"are more than your title?",
"As a noble Lord of the Royal Court, you will be unused to the wilderness so this will be a challenge. Can you prove you "
"are more than your title?",
"As a mere Squire, can you become more than what you were born to be?",
"You may be a mere villager but you have never left the confines of your village. How will you cope with the big world "
"out there?",
"You are a Witch (in training). WIll you have what it takes to become a true Witch?",
"You are a Wizard (in training). Will you have what it takes to become a true Wizard?",
];


#function which gives player another chance to check the info a specific rank after doing it once.

def rankListCheck(ans):

    while ans == "y" or ans == "yes":
        rank = input("Choose another rank:\n").title()
        time.sleep(ts750ms)
        rank = rankCheck(rank)
        rankSentence = rankDeclare(rank)
        print(rankSentence)
        time.sleep(ts750ms)
        print("Would you like to choose another?")
        ans = input("Choose (Y)es or (N)o?\n").lower()
    if ans == "n" or ans == "no":
        rank = input("Pick a rank: \n").title()
        rank = rankCheck(rank)
        return rank

#function which check if rank exists

def rankCheck(rank):
    while rank not in rankList:
        rank = input("Invalid choice. Choose a valid choice.\n").title()
    else:
        return rank

#function which prints out description of rank once rank is decided


def rankDeclare(rank):

    count = 0

    if rank == rankList[count]:
        i = count
        rankFinal = rankDesc[i]
        return(rankFinal)

    while rank != rankList[count]:
        count = count + 1
        if rank == rankList[count]:
            i = count
            rankFinal = rankDesc[i]
            return(rankFinal)
