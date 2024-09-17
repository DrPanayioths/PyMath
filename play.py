import os
import time
import random
import time
import re


# Main Area
os.system('color b')
print("Do You Know Math?" + " | By DrPanayioths")
time.sleep(2)
print("")

# Difficutly Selector
print("1 - 🟢 Beginner [+,-]")
print("2 - 🟡 Intermediate [*,+,-]")
print("3 - 🔴 Advanced [*,/,+,-]")
difficulty_selected = input("Select Difficulty: ")


# Main Game
   
def difficatly_1(): 
    number = random.randrange(0,200)
    number2 = random.randrange(0,200)
    print(f"{number} + {number2}")
    result = input("Answer: ")
    
    if re.search(r'[A-Za-z]', result):
        print("")
        print("!!Enter Only Numbers!!")
        print("")
        difficatly_1()
    elif not result.strip():
        print("")
        print("!!Type A Number!!")
        print("")
        difficatly_1()
        
    # If All Checks Are Passed Code Run    
    else:
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
            print("")
            print("Refresh In" + " 2s |" " Ctrl + C to exit")
            time.sleep(1)
            print("Refresh In" + " 1s |" " Ctrl + C to exit")
            time.sleep(1)
            print("")
            difficatly_1()
    

        
        
        
def difficatly_2(): 
    number = random.randrange(0,500)
    number2 = random.randrange(0,500)
    multiply = random.randrange(0,8)
    minus = random.randrange(0, number + number2)
    print(f"{number} * {multiply} + {number2} - {minus}  ")
    result = input("Answer: ")
    
    if re.search(r'[A-Za-z]', result):
        print("")
        print("!!Enter Only Numbers!!")
        print("")
        difficatly_2()
    elif not result.strip():
        print("")
        print("!!Type A Number!!")
        print("")
        difficatly_2()
        
    # If All Checks Are Passed Code Run    
    else:
        if (int(result) == (number * multiply + number2 - minus )):
            print("You Got It Right!, This Was Hard")
            print("")
            print("Refresh In" + " 2s |" " Ctrl + C to exit")
            time.sleep(1)
            print("Refresh In" + " 1s |" " Ctrl + C to exit")
            time.sleep(1)
            print("")
            difficatly_2()
        else:
            print("You Tried But You Are Wrong!")
            
            print("Refresh In" + " 2s |" " Ctrl + C to exit")
            time.sleep(1)
            print("Refresh In" + " 1s |" " Ctrl + C to exit")
            time.sleep(1)
            print("")
            difficatly_2()
    
def difficatly_3():
    number = random.randrange(0,500)
    number2 = random.randrange(0,500)
    multiply = random.randrange(0,8)
    minus = random.randrange(0, number + number2)
    divide = random.randrange(0,2)
    print(f"{number} * {multiply} + {number2} - {minus} - {divide} * 2 ")
    result = input("Answer: ")
    
    if re.search(r'[A-Za-z]', result):
        print("")
        print("!!Enter Only Numbers!!")
        print("")
        difficatly_3()
    elif not result.strip():
        print("")
        print("!!Type A Number!!")
        print("")
        difficatly_3()
        
    # If All Checks Are Passed Code Run    
    else:
        if (int(result) == (number * multiply + number2 - minus / divide * 2 )):
            print("You Got It Right!, This Was Hard")
            print("")
            print("Refresh In" + " 2s |" " Ctrl + C to exit")
            time.sleep(1)
            print("Refresh In" + " 1s |" " Ctrl + C to exit")
            time.sleep(1)
            print("")
            difficatly_3()
        else:
            print("You Tried But You Are Wrong!")
            
            print("Refresh In" + " 2s |" " Ctrl + C to exit")
            time.sleep(1)
            print("Refresh In" + " 1s |" " Ctrl + C to exit")
            time.sleep(1)
            print("")
            difficatly_3()
             









# run the correct function
if (difficulty_selected == "1"):
    difficatly_1()
elif (difficulty_selected == "2"):
    difficatly_2()
elif (difficulty_selected == "3"):
    difficatly_3()
