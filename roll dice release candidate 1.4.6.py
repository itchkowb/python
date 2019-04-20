#129 lines (65 sloc)  2.65 KB

minimum_die_number = 1
maximum_die_number = 12

#if maximum_die_number <= 11:
    #set variable to 12
#else:
   #pass

print("-----------------------")                  #Displays title art
print("~~~~~ROLL THE DICE~~~~~")
print("-----------------------")
begin_prompt = raw_input("Are you ready? (y/N) ") #Initializes the script


if begin_prompt == "y":                           #If the user inputs the letter y, continue
    pass
elif begin_prompt != "N":
    print("I didn't understand that, please restart the program")
    exit()
else:                                             #If the user inputs something else
    print("Ok, bye")                              #Bid the user adue
    exit()                                        #Quit the script

from random import *                              #Get random number, assign it the "numb" variable
numb = randint(minimum_die_number, maximum_die_number) 


if numb == 1:                                     #If the number rolled is a 1, write this
     print("--------------")
     print("|             |")
     print("|             |")
     print("|      *      |       You rolled a 1!")
     print("|             |")
     print("|             |")
     print("--------------")
elif numb == 2:                                   #If the number rolled is a 2, write this
     print("--------------")
     print("| *           |")
     print("|             |")
     print("|             |       You rolled a 2!")
     print("|             |")
     print("|          *  |")
     print("--------------")
elif numb == 3:                                   #If the number rolled is a 3, write this
     print("--------------")
     print("| *           |")
     print("|             |")
     print("|      *      |       You rolled a 3!")
     print("|             |")
     print("|          *  |")
     print("--------------")
elif numb == 4:                                   #If the number rolled is a 4, write this
     print("--------------")
     print("| *        *  |")
     print("|             |")
     print("|             |       You rolled a 4!")
     print("|             |")
     print("| *        *  |")
     print("--------------")
elif numb == 5:                                   #If the number rolled is a 5, write this
     print("--------------")
     print("| *        *  |")
     print("|             |")
     print("|      *      |       You rolled a 5!")
     print("|             |")
     print("| *        *  |")
     print("--------------")
elif numb == 6:                                   #If the number rolled is a 6, write this
     print("--------------")
     print("| *        *  |")
     print("|             |")
     print("| *        *  |       You rolled a 6!")
     print("|             |")
     print("| *        *  |")
     print("--------------")
elif numb == 7:                                   #If the number rolled is a 7, write this
     print("---------------    ---------------")
     print("|             |    | *          * |")
     print("|             |    |              |")
     print("|      *      |    | *          * |       You rolled a 7!")
     print("|             |    |              |")
     print("|             |    | *          * |")
     print("---------------    ----------------")
elif numb == 8:                                   #If the number rolled is an 8, write this
     print("---------------    ---------------")
     print("| *           |    | *          * |")
     print("|             |    |              |")
     print("|      *      |    |       *      |      You rolled an 8!")
     print("|             |    |              |")
     print("|          *  |    | *          * |")
     print("---------------    ---------------")
elif numb == 9:                                   #If the number rolled is a 9, write this
     print("---------------    --------------")
     print("| *         * |    | *         * |")
     print("|             |    |             |")
     print("|      *      |    |             |       You rolled a 9!")
     print("|             |    |             |")
     print("| *        *  |    | *         * |")
     print("---------------    --------------")
elif numb == 4:                                   #If the number rolled is a 10, write this
     print("---------------    ---------------")
     print("| *         * |    | *          * |")
     print("|             |    |              |")
     print("|      *      |    |      *       |      You rolled a 10!")
     print("|             |    |              |")
     print("| *         * |    | *          * |")
     print("---------------    ----------------")
elif numb == 11:                                   #If the number rolled is an 11, write this
     print("---------------    ---------------")
     print("| *        *  |    | *          * |")
     print("|             |    |              |")
     print("| *        *  |    |      *       |    You rolled an 11!")
     print("|             |    |              |")
     print("| *        *  |    | *          * |")
     print("---------------    ---------------")
elif numb == 12:                                   #If the number rolled is a 12, write this
     print("--------------     ---------------")
     print("| *        *  |    | *          * |")
     print("|             |    |              |")
     print("| *        *  |    | *          * |    You rolled a 12!")
     print("|             |    |              |")
     print("| *        *  |    | *          * |")
     print("---------------    ---------------")
     
else:
    exit()
