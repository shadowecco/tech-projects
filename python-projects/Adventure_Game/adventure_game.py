"""
Original idea started by FreeCodeCamp.
This version was developed by Helen Yates
Copyright 2020

This was a small cute little project started by FreeCodeCamp but the original
file focused on input as well as conditions. I am constantly expanding it to
include imported programs and functions.

Added comments to this new path so it can be easy to see the progress paths so
it'd be easier to go look on different paths

Comments in Upper Case reflect to the path of the game. Others are personal
notes.
"""

import time

#Time functions so the screen doesn't become overloaded with text too quickly.

ts1 = 1

#Function to check guesses of riddles

def check_guess(guess, riddle_answer):

    guess_lives=2
    guess_attempts=0

    while guess_lives > 0:
        if guess.lower() != riddle_answer.lower():
            guess_lives-=1;
            guess_attempts+=1;
            guess_modify=(guess_attempts+1)
            lives_modify=(guess_lives+1)
            print("Wrong!")
            time.sleep(ts1)
            print("You have" ,lives_modify, "attempts left.")
            time.sleep(ts1)
            guess=input("Try again.\n")
            if guess.lower() != riddle_answer.lower() and guess_lives==0:
                print("Sorry. You have 0 attempts left.")
                return guess_lives
            elif guess.lower() == riddle_answer.lower() and guess_attempts >= 1:
                guess_attempts+=1
                print("Yeah. You did it in" ,guess_attempts, "attempts.")
                return guess_attempts
        elif guess.lower() == riddle_answer.lower():
            guess_attempts+=1;
            if guess_attempts == 1:
                print("Yeah. You did it in 1 attempt! You're a smart cookie!")
                return guess_attempts
            elif guess_attempts < 1:
                print("Yeah. You did it in" ,guess_attempts, "attempts.")
                return guess_attempts


#Just to avoid repetition of answers and to simplify

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_yes = ["Y", "YES", "y", "yes"]
answer_no = ["N", "NO", "n", "no"]
answer_left = ["l", "left",]
answer_right = ["r", "right",]


#Lists of ranks that player can currecntly play as. More can be added and
#they will be automatically added onto when the choice of rank comes up. 


rankList= ["Lord", "Lady", "Knight", "Squire"];

#Number of health points the player starts with.

health = 10


#Number of attempts in tackling riddles. They start at 2 so it can get down to 0 in 3 attempts.
#Numbers start with 0 so starting at 3 brings 4 attempts.


troll_riddle_count=2

#Welcome

print("Welcome to this adventure game")
time.sleep(ts1)
age = int(input("What is your age?\n"))


#AGE PATH - ARE THEY 18 OR OLDER?
#AGE PATH A - IF THEY ARE OVER 18


if age >= 18:
    print("Yeah! You are old enough to play!")
    wants_to_play = input("Do you want to play?\n")

#GAME PATH 1A - CHOICE OF PLAY. THIS PATH FOLLOWS IF THE PLAYER STATES YES
    
    if wants_to_play in answer_yes:
        
#Name Generator. This is arranged so no matter what the player writes,
#whether it's all capitals or a mixture, the final structure will always be
#lower case except for the first letter which will be capitalised.

        
        name = input("Enter your name here:\n").title()


#Rank Generator. This is arranged so that the player can only choose
#only one of four types of characters and a loop will happen until the player
#chooses one from the list.
#Once again, no matter how the player types it, the result will always
#be lowercase with the first letter being capitalised.


        print("Now you need to pick a rank. Here are your choices: ")
        print(*rankList, sep= "/")
        time.sleep(ts1)
        rank = input("Choose a rank: \n").title()
        while rank not in rankList:
            rank = input("Invalid choice. Please try again.\n").title()
            if rank in rankList:
                break
        if rank in rankList:
            print("Welcome to the mythical kingdom of Ravenbrooke," + " " + rank + " " + name,".")
            time.sleep(ts1)
            print("You are staring with", health, "health")
            time.sleep(ts1)
            print("Let's play!")
            time.sleep(ts1)
            print("You were minding your business when POOF! You are transported into the middle of a dark forest. There is a long road with signs pointing to the left and the right.")
            time.sleep(ts1)
            
#GAME PATH 2 - DOES THE PLAYER GO LEFT OR RIGHT?

            left_or_right = input("So, do you choose left or right (Choose L for Left and R for Right)?\n").lower()


#GAME PATH 2 - IF PLAYER CHOOSES SOMETHING OTHER THAN L OR R 
#This part was really tricky. I wanted it so the only option can be A or B
#and then if the player choose something else, they would be stuck in a loop
#until they did.
#I tried to apply the same logic that I did for the rank part above the logic
#of using the lists and OR kept failing so this was the best method I could
#come up with. 
#There was an attempt to make this into a function so it can be replicated with
#little code but it didn't work.


            while left_or_right != "l" and left_or_right != "left" and left_or_right !=  "r" and left_or_right != "right":
                left_or_right = input("Invalid choice. Choose Left or Right.\n").lower()
            
                
#PATH 2A - IF THE PLAYER GOES LEFT
                
            if left_or_right in answer_left:
                print("Okay so you follow the path and reach a lake. Do you swim across or go around?")
                time.sleep(ts1)
                lake_ans = input("Choose A for across or B for around: \n")
                
#GAME PATH 3 - IF PLAYER CHOOSES SOMETHING OTHER THAN A OR B
                
                while lake_ans != "a" and lake_ans != "A" and lake_ans != "b" and lake_ans != "B":
                    lake_ans = input("Invalid choice. Choose A or B.\n").lower()

#GAME PATH 3A - IF PLAYER SWIMS ACROSS THE RIVER- ENDS UP AT PATH 4
                    
                if lake_ans in answer_A:
                    print("You managed to get across, but you were bit by a fish and lost 5 health.")
                    health -= 5
                    time.sleep(ts1)
                    print("You have", health, "health left. Be careful with your next move.")

#GAME PATH 3B - IF PLAYER GOES AROUND THE LAKE - ENDS UP AT PATH 4

                if lake_ans in answer_B:
                    print("You went around and reached the other side of the lake.")

#GAME PATH 4 - RIVER OR HOUSE
                    
                time.sleep(ts1)
                print("You notice a house and a river.")
                time.sleep(ts1)
                hr_ans = input("Which do you go to? (Choose A for river or B for house)?\n").lower()

#GAME PATH 4 - IF PLAYER CHOOSES SOMETHING OTHER THAN A OR B 

                while hr_ans != "a" and hr_ans != "A" and hr_ans != "b" and hr_ans != "B":
                    hr_ans = input("Invalid choice. Choose A or B.\n").lower()

#GAME PATH 4A - IF PLAYER CHOOSES A

                if hr_ans in answer_A:
                    print("You walk along until you see a acrap piece of paper saying:")
                    time.sleep(ts1)
                    print("'Turn the letters around and find its partner.'")
                    time.sleep(ts1)

#GAME PATH 5 - TROLL RIDDLE
                    
                    print("You put the piece of paper in your pocket and keep walking. A while later, you find yourself at a bridge with a troll-like creature standing before it.")
                    time.sleep(ts1) 
                    print("The troll cries out, 'You can only pass me if you solve the riddle of the bridge.")
                    time.sleep(ts1)
                    print("...solve it and you may pass. Fail and I kill you.")
                    time.sleep(ts1)
                    print("...you have three attempts.'")
                    time.sleep(ts1)
                    print("He points to a sign which says 'TL ZDZB GILOO'")
                    time.sleep(ts1)

#GAME PATH 5 - WHAT HAPPENS IF PLAYER GUESSES INCORRECTLY AND THERE ARE STILL
#ATTEMPTS LEFT


                    troll_riddle=input("Enter your answer:\n").lower()
                    troll_attempts = check_guess(troll_riddle, "go away troll")
                    
#GAME PATH 5A - IF GUESSES CORRECTLY

                    if troll_attempts >= 1:
                        print("You did it! The troll throws a tantrum but he allows you to pass.")
                        time.sleep(ts1)
                        print("As he stomps off, he drops some black apples.")
                        time.sleep(ts1)

#GAME PATH 6 - EATING APPLES 

                        food_choice=input("Do you eat one? (Y)es/(N)o\n").lower()

#GAME PATH 6A - IF ANSWER IS NO

                        if food_choice in answer_no:
                            print("Very wise. They look poisonous anyway. You walk across the bridge and see many apple trees. You pick one and eat it. You gained 5 health.")
                            health +=5
                            time.sleep(ts1)
                            print("You now have", health, "health")
                            time.sleep(ts1)

#GAME PATH 6B - IF ANSWER IS YES
                            
                        if food_choice in answer_yes:
                            print("Oh No! The apple was posionous and you lose 5 health")
                            health -=5
                            time.sleep(ts1)
                            print("You now have", health, "health")
                            time.sleep(ts1)
                            if health == 0:
                                print("You lost. Game over.")
                            if health <=5:
                                time.sleep(ts1)
                                print("Your health is low. Be careful.")

#GAME PATH 7 - NEW PATH

                        print("The path is unclear to you. Maybe the path will open to you one day.")
                        

#GAME PATH 5A - IF GUESSES INCORRECTLY

                    if troll_attempts==0:
                        print("The troll laughs at you and knocks you out with a very large club. You lose your health and die.")
                        time.sleep(ts1)
                        print("You lost. Game over.")
                    

#GAME PATH 4B - IF PLAYER CHOOSES B - POSSIBLE OPPORTUNITY FOR EXPANSION
                    

                if hr_ans in answer_B:
                    print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health")
                    health -= 5
                    time.sleep(ts1)
                    print("You now have", health, "health")
                    time.sleep(ts1)
                    if health == 0:
                        print("You lost. Game over.")
                    if health >= 5:
                        print("The path is unclear to you. Maybe the path will open to you one day.")

                    
#GAME PATH 2B - IF THE PLAYER GOES RIGHT

            elif left_or_right in answer_right:
                print("The path is unclear to you. Maybe the path will open to you one day.")

   
#PATH 1B - CHOICE OF PLAY. THIS PATH FOLLOWS IF THE PLAYER STATES NO
#This is subject to change. At the moment I'm focusing on what happens if
#the player chooses left. 

        
    else:
        print("Okay. Bye, then.")

#AGE PATH B - IF THEY ARE UNDER 18
else:
    print("Sorry. You are not old enough to play.")
