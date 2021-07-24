#Based on a name generator game from the late 90s/early 00s where
#you can retrieve your Star Wars name by using this method:

#First name: 
#First 3 letters of your last name
#+ First 2 letters of your first name

#Last name:
#First 2 letters of your mother's maiden name
#+ First 3 letters of the town you were born in

import random
import time

ts1 = 1

alliance_list = ["Jedi", "Sith", "Neutral", "Rebel Alliance", "Galactic Empire", "Resistance", "First Order"]

alliance_choice = (random.choice(alliance_list))

f_name=input("What is your first name?\n").lower()
l_name=input("What is your last name?\n").title()
m_name=input("What is your mother's maiden name?\n").title()
b_town=input("What is the town you were born in?\n").lower()

l_name_3 = l_name[:3]
f_name_2 = f_name[:2]
m_name_2 = m_name[:2]
b_town_3 = b_town[:3]

sw_fname = l_name_3 + f_name_2 
sw_lname = m_name_2 + b_town_3

print("Your Star Wars name is", sw_fname, sw_lname,)
time.sleep(ts1)
if alliance_choice == "Neutral":
    print("Your alliance is Neutral.") 
else:
    print("Your alliance is with the", alliance_choice)