#Project: Rock - Paper - Scissors Game

import random

print ("""Winning Rules \n
       "Rock vs Paper => Paper wins"\n
       "Rock vs Scissors => Rock wins"\n
       "Paper vs Scissors => Scissors wins""")

while True:
    print("Enter Choice: 1. Rock 2. Paper 3. Scissors")
    
    user_choice = int(input("User Turn: "))
    
    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("Enter valid input: "))
        
    if user_choice == 1:
        user_choice_name = "Rock"
    
    elif user_choice == 2:
        user_choice_name = "Paper"
    
    else: 
        user_choice_name = "Scissors"
    
    print("User Choice is: " + user_choice_name)
    print ("\nIt is now computer's turn")
    
    comp_choice = random.randint(1,3)
    
    while comp_choice == user_choice:
        comp_choice = random.randint(1,3)
        
    if comp_choice == 1:
        comp_choice_name = "Rock"
    
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    
    else:
        comp_choice_name = "Scissors"
    
    print("Computer choice is: " + comp_choice_name)
    print(user_choice_name + "vs" + comp_choice_name)
    
    if ((user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 1)):
        print("Paper wins =>", end = "")
        result = "Paper"    
        
    elif ((user_choice == 1 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1)):
        print("Rock wins =>", end = "")
        result = "Rock"
        
    else:
        print("Scissors wins =>", end = "")
        result = "Scissors"
    
    if result == user_choice_name:
        print("** User wins!! **")
    
    else:
        print("** Computer wins!! **")

    print("Do you want to play again? (Y/N)")
    ans = input()
    
    if ans == 'n' or ans == 'N':
        break
    print("Thanks for playing")
    
        
        
        
