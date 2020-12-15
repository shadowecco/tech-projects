#Original idea started by FreeCodeCamp.
#This version was developed by Helen Yates
#Copyright 2020

import sys
import time

sa = 1

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_yes = ["Y", "YES", "y", "yes"]
answer_no = ["N", "NO", "n", "no"]
answer_left = ["l", "left",]
answer_right = ["r", "right",]
answer_riddle = ["go away troll"]

rankList= ["Lord", "Lady", "Knight", "Squire"];

health = 10

print("Welcome to this adventure game")
time.sleep(sa)
age = int(input("What is your age?\n"))

if age >= 18:
    print("Yeah! You are old enough to play!")
    wants_to_play = input("Do you want to play?\n")
    if wants_to_play in answer_yes:
        name = input("Enter your name here:\n").lower()
        nameReturned = name.capitalize()
        print("Now you need to pick a rank. Here are your choices: ")
        print(*rankList, sep= "/")
        time.sleep(sa)
        rank = input("Choose a rank: ").lower()
        rankReturned = rank.capitalize()
        while rankReturned not in rankList:
            rankReturned = input("Invalid choice. Please try again.\n").lower()
            rankReturned = rankReturned.capitalize()
            if rankReturned in rankList:
                break
        if rankReturned in rankList:
            print("Welcome to the mythical kingdom of Ravenbrooke," + " " + rankReturned + " " + nameReturned,".")
            time.sleep(sa)
            print("You are staring with", health, "health")
            time.sleep(sa)
            print("Let's play!")
            time.sleep(sa)
            print("You were minding your business when POOF! You are transported into the middle of a dark forest. There is a long road with signs pointing to the left and the right.")
            time.sleep(sa)
            left_or_right = input("So, do you choose left or right (Choose L for Left and R for Right)?\n").lower()
            while left_or_right != "l" and left_or_right != "left" and left_or_right !=  "r" and left_or_right != "right":
                left_or_right = input("Invalid choice. Choose Left or Right.\n").lower()
            if left_or_right in answer_left:
                print("Okay so you follow the path and reach a lake. Do you swim across or go around?")
                time.sleep(sa)
                lake_ans = input("Choose A for across or B for around: ")
                while lake_ans != "a" and lake_ans != "A" and lake_ans != "b" and lake_ans != "B":
                    lake_ans = input("Invalid choice. Choose A or B.\n").lower()  
                if lake_ans in answer_A:
                    print("You managed to get across, but you were bit by a fish and lost 5 health.")
                    health -= 5
                    time.sleep(sa)
                    print("You have ", health, "health left. Be careful with your next move.")
                if lake_ans in answer_A:
                    print("You went around and reached the other side of the lake.")
                time.sleep(sa)
                print("You notice a house and a river.")
                time.sleep(sa)
                hr_ans = input("Which do you go to? (Choose A for river or B for house)?\n").lower()
                while hr_ans != "a" and hr_ans != "A" and hr_ans != "b" and hr_ans != "B":
                    hr_ans = input("Invalid choice. Choose A or B.\n").lower()
                if hr_ans in answer_A:
                    print("You walk along until you see a acrap piece of paper saying:")
                    time.sleep(sa)
                    print("Turn the letters around and find its partner.")
                    time.sleep(sa)
                    print("You put the piece of paper in your pocket and keep walking. A while later, you find yourself at a bridge with a troll-like creature standing before it.")
                    time.sleep(sa) 
                    print("The troll cries out, 'You can only pass me if you solve the riddle of the bridge. Solve it first time and you may pass. Fail and I kill you.'")
                    time.sleep(sa)
                    print("He points to a sign which says 'TL ZDZB GILOO'")
                    time.sleep(sa)
                    riddle_ans=input("Enter your answer:\n").lower()
                    if riddle_ans in answer_riddle:
                        print("You did it! The troll throws a tantrum but he allows you to pass.")
                        time.sleep(sa)
                        print("As he stomps off, he drops some black apples.")
                        time.sleep(sa)
                        food_choice=input("Do you eat one? (yes/no)\n").lower()
                        if food_choice in answer_no:
                            print("Very wise. They look poisonous anyway. You walk across the bridge and see many apple trees. You pick one and eat it. You gained 5 health.")
                            health +=5
                            time.sleep(sa)
                            print("You now have", health, "health")
                        if food_choice in answer_yes:
                            print("Oh No! The apple was posionous and you lose 5 health")
                            health -=5
                            time.sleep(sa)
                            print("You now have", health, "health")
                            if health == 0:
                                print("You lost. Game over.")
                    else:
                        print("The troll laughs at you and knocks you out with a very large club. You lose your health and die.")
                        time.sleep(sa)
                        print("You lost. Game over.")
                if hr_ans in answer_B:
                    print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health")
                    health -= 5
                    time.sleep(sa)
                    print("You now have", health, "health")
                    time.sleep(sa)
                    if health == 0:
                        print("You lost. Game over.")
            elif left_or_right in answer_right:
                print("You fell down and lost...") 
    else:
        print("Okay. Bye, then.")
else:
    print("Sorry. You are not old enough to play.")
