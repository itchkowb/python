#72 lines (65 sloc)  2.49 KB
  
print("-----------------------")
print("~~~~~ROLL THE DICE~~~~~")
print("-----------------------")
begin_prompt = raw_input("Are you ready? (y/N) ")  #Initializes the script


if begin_prompt == "y":                           #If the user inputs the letter y, continue
    pass
elif begin_prompt != "N":
    print("I didn't understand that, please restart the program")
    exit()
else:                                             #If the user inputs something else
    print("Ok, bye")                              #Bid the user adue
    exit()                                        #Quit the script


from random import *                              #Get random number, assign it the "numb" variable
numb = randint(1, 6) 

if numb == 1:                                     #If the random numer is 1, write this
    print("--------------")
    print("|             |")
    print("|             |")
    print("|      *      |       You rolled a 1!")
    print("|             |")
    print("|             |")
    print("--------------")
elif numb == 2:                                   #If the random numer is 2, write this
     print("--------------")
     print("| *           |")
     print("|             |")
     print("|             |       You rolled a 2!")
     print("|             |")
     print("|          *  |")
     print("--------------")
elif numb == 3:                                   #If the random numer is 3, write this
     print("--------------")
     print("| *           |")
     print("|             |")
     print("|      *      |       You rolled a 3!")
     print("|             |")
     print("|          *  |")
     print("--------------")
elif numb == 4:                                   #If the random numer is 4, write this
     print("--------------")
     print("| *        *  |")
     print("|             |")
     print("|             |       You rolled a 4!")
     print("|             |")
     print("| *        *  |")
     print("--------------")
elif numb == 5:                                   #If the random numer is 5, write this
      print("--------------")
      print("| *        *  |")
      print("|             |")
      print("|      *      |       You rolled a 5!")
      print("|             |")
      print("| *        *  |")
      print("--------------")
elif numb == 6:                                   #If the random numer is 6, write this
     print("--------------")
     print("| *        *  |")
     print("|             |")
     print("| *        *  |       You rolled a 6!")
     print("|             |")
     print("| *        *  |")
     print("--------------")
else:
    exit()
