import os
import time
import random
import time


# Main Area
os.system('color b')
print("Do You Know Math?" + " | By DrPanayioths")
time.sleep(2)
print("")

# Difficutly Selector
print("1 - Easy")
print("2 - Medium")
print("3 - Hard")
difficulty_selected = input("Select Difficulty: ")


# Main Game
   
def difficatly_1(): 
    number = random.randrange(0,200)
    number2 = random.randrange(0,200)
    print(f"{number} + {number2} = ")
    result = input("Answer: ")
    
    if (int(result) == (number + number2)):
        print("Nice Job! Lets Contine")
        print("")
        print("Refresh In" + " 2s |" " Ctrl + C to exit")
        time.sleep(1)
        print("Refresh In" + " 1s |" " Ctrl + C to exit")
        time.sleep(1)
        print("")
        difficatly_1()
    else:
        print("Wrong Answer!, But Nice Try")
        
        print("Refresh In" + " 2s |" " Ctrl + C to exit")
        time.sleep(1)
        print("Refresh In" + " 1s |" " Ctrl + C to exit")
        time.sleep(1)
        print("")
        difficatly_1()
         









# run the correct function
if (difficulty_selected == "1"):
    difficatly_1()
