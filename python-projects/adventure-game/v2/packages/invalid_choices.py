#Python functions

import time

ts750ms = 750/1000 #750 milliseconds
ts1s = 1 #1 second

#Brings back invalid choice if a or b is not picked 

def invalid_ab(ans):

    while ans != "a" and ans != "b": 
        ans = input("Invalid choice. Choose A or B.\n").lower()
        time.sleep(ts750ms)
    if ans == "a" or ans == "b":
        return ans

#Brings back invalid choice if a, b or c is not picked 

def invalid_abc(ans):

    while ans != "a" and ans != "b" and ans != "c": 
        ans = input("Invalid choice. Choose A, B or C.\n").lower()
        time.sleep(ts750ms)
        if ans == "a" or ans == "b" or ans == "c":
            return ans
        break
      
#Brings back invalid choice if m or f is not picked 

def invalid_mf(ans):

    while ans != "m" and ans != "male" and ans != "f" and ans != "female": 
        ans = input("Invalid choice. Choose M or F.\n").lower()
        time.sleep(ts750ms)
        if ans == "m" or ans == "male" or ans == "f" or ans == "female":
            return ans

#Brings back invalid choice if y or n is not picked 

def invalid_yn(ans):

    while ans != "y" and ans != "yes" and ans != "n" and ans != "no": 
        ans = input("Invalid choice. Choose y or n.\n").lower()
        time.sleep(ts750ms)
        if ans == "y" or ans == "yes" or ans == "n" or ans == "yes":
            return ans

# Brings back invalid choice if valid item from house is not picked

def invalid_collect_item(collect_item):

    while house_item != "beans" and house_item != "apple" and house_item != "sword" and house_item != "wand":
        house_item = input("Invalid choice. Choose one of the items.\n").lower()
        time.sleep(ts750ms)
        if house_item == "beans" or house_item == "apple" or house_item == "sword" or house_item == "wand":
            return house_item






