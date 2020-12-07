#This was a small cute little project started by FreeCodeCamp but the original file focused on input as well as conditions. I am constantly expanding it to include imported programs and functions.

#Took out the functions as the rank and name may become relevant in the game and it would be hard to retrieve via a function. Basically, it's the same principles of upper and lower case but outisde a function.  


print("Welcome to this adventure game")
age = int(input("What is your age? "))

health = 10

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ")
    if wants_to_play == "yes":
        name = input("Enter your name here: ").lower()
        nameReturned = name.capitalize()
        rank = input("Now we need to know your rank. Are you a Lord, Lady, Knight or Squire? (Choose One.) Enter here: ").lower()
        rankReturned = rank.capitalize()
        print("Welcome to the mythical kingdom of Ravenbrooke," + " " + rankReturned + " " + nameReturned,".") 
        print("You are staring with", health, "health")
        print("Let's play!")
        print("You were minding your business when POOF! You are transported into the middle of a dark forest. There is a long road with signs pointing to the left and the right.")

        left_or_right = input("Do you choose left or right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5

            ans = input("You notice a house and a river. Which do you go to (river/house)? ")
            if ans == "house":
                print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health")
                health -= 5
                
            elif ans == "river":
                print("You walk along until you see a acrap piece of paper saying:") 
                print("Turn the letters around and find its partner.")
                print("You put the piece of paper in your pocket and keep walking. A while later, you find yourself at a bridge with a troll-like creature standing before it.")
                print("The troll cries out, 'You can only pass me if you solve the riddle of the bridge. Solve it first time and you may pass. Fail and I kill you.'")
                print("He points to a sign which says 'TL ZDZB GILOO'")
                
                riddle_ans1=input("Enter your answer: ") 
                if riddle_ans1 == "Go away troll":
                    print("You did it! The troll throws a tantrum but he allows you to pass.")
                    print("As he stomps off, he drops some black apples.")
   
                    food_choice=input("Do you eat one? (yes/no)")
                    if food_choice == "no":
                        print("Very wise. They look poisonous anyway. You walk across the bridge and see many apple trees. You pick one and eat it. You gained 5 health.")
                        health +=5
                        print("You now have", health, "health")
                    else:
                        print("Oh No! The apple was posionous and you lose 5 health")
                        health -=5
                        
                else:
                    print("The troll laughs at you and knocks you out with a very large club. You lose your health and die.")
                    print("You lost the game.")
 

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived... You win!")

            else:
                print("You fell in the river and lost...")


        else:
            print("You fell down and lost...")

    else:
        print("Cya...")
else:
    print("You are not old enough to play...")
