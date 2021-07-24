import random
import time

ts1 = 1

person1 = input("What is your name?\n");
person2 = input("What is your crush's name?\n");
loveScore = random.randint(1,101);
print("Your love score is", loveScore, "%!")
time.sleep(ts1)

if loveScore >= 80:
    print("You love each other like Kanye loves Kanye!")
elif loveScore >= 60:
    print("There is a connection there. Maybe it can lead to love.")
elif loveScore >= 40:
    print("Hmmmm maybe stick to being friends.")
elif loveScore >= 20:
    print("Your connection is as cold as ice.")
else:
    print("You are like chalk and cheese.")


