#DOC333 Coursework python code
#Name-Chenuka Sarathchandra
#student ID- 20221022

#intialising the variables

Student_name=""
attemptNo=0
option=""
numL=[]
guessL=[]
resultL=[]
result=0
repeat=0
count=8


#Making the User interface of the game

#getting the student name to be displayed
Student_name=str(input("Pls enter your name : "))
print("                                               Hi",Student_name,"  Welcome to GameInt")

print("Number to guess - XXXX","                                                                       Colour mapping: 1-White 2-Blue 3-Red 4-Yellow 5-Green 6-Purple")
#Preparing the menu for the gamer to start or quit the game
option = input("Do you want to begin the game ? (yes/no)-")
option.lower()
if (option=="no"):
    print("Program terminated ! thank you for playing ")
    exit()
while option not in ("yes", "no"):
    print("invalid input pls enter again - ")
    option = input("Do you want to begin the game? (yes/no) ?- ")
    option.lower()
    if (option == "no"):
        print(" Thank you for playing and have a great day !")
        attemptNo = 9
        exit()


#Generating a random number for the student to guess
import random
numL= random.choices([1, 2, 3, 4, 5, 6], k=4) #Random number wont be shown in the actual game but can be shown in order to test the program

#getting user input
while(attemptNo!=count)or(option=="yes"):
    try:
        guess1=int(input("Enter your guess for the first digit in the code :"))
        guess2=int(input("Enter your guess for the second digit in the code :"))
        guess3=int(input("Enter your guess for the third digit in the code :"))
        guess4=int(input("Enter your guess for the forth digit in the code :"))
        guessL=[guess1,guess2,guess3,guess4]
    except ValueError:
            print("Invalid value") # validates user inputs incase they enter datatypes apart from integer .
            continue
    #resetting temp variables
    resultL.clear()
    repeat=0


#validating whether the gamer entered the data in the correct rangefor i in range(4):
    for i in range(4):
        if(guessL[i]<1 or guessL[i]>6):
            print("Data entered as guess is not in the correct range pls re-enter, you will be given an extra attempt")
            repeat=1
            
     
    if(guessL==numL):
        print("attemptNo-",attemptNo+1,"    guess-",guessL,"       Result-","1"*4)
        print("Congratulations  You have won the game…  You have scored XXX points.")
        option = input("Do you want to play another round ? (yes/no):")
        option.lower()
        while option not in ("yes", "no"):
            print("invalid input pls enter again : ")
            option = input("Do you want to begin the game? (yes/no) ?-")
            option.lower()
     
        if (option == "yes"):
            attemptNo=-1
            #Generating a random number for the student to guess
            numL= random.choices([1, 2, 3, 4, 5, 6], k=4)
            resultL.clear()
            guessL.clear()
        elif (option == "no"):
            print(" Thank you for playing and have a great day !")
            exit()

    elif (guessL ==[0,0,0,0]): # user can enter this to terminate the program
        print(" Program terminated ! thank you for playing ")
        attemptNo = 9
        exit()
            
    elif(attemptNo==count):
        print(" Number of Attempts are over ")
        option = input("Do you want to play another round ? (yes/no):")
        option.lower()
        while option not in ("yes", "no"):
            print("invalid input pls enter again : ")
            option = input("Do you want to begin the game? (yes/no) ?-")
            option.lower()
        
        if (option == "yes"):
            attemptNo=-1
            resultL.clear()
            guessL.clear()
            #Generating a random number for the student to guess
            numL= random.choices([1, 2, 3, 4, 5, 6], k=4)
        elif (option == "no"):
            print(" Thank you for playing and have a great day !")
            exit()

    else:
            
            if guessL[0]==numL[0]:
                resultL.append(1)# finding numbers in correct positions in order to make the result ("1")
            elif guessL[0] in numL:
                resultL.append(0) # ("0") will be printed to tell the student the number is correct but is in the wrong postion
            else:
                resultL.append('.') # (".") will be printed to tell the user the number he guesses is not correct
        
            if guessL[1]==numL[1]:
                resultL.append(1)
            elif guessL[1] in numL:
                resultL.append(0)
            else:
                resultL.append('.')

            if guessL[2]==numL[2]:
                resultL.append(1)
            elif guessL[2] in numL:
                resultL.append(0)
            else:
                resultL.append('.')

            if guessL[3]==numL[3]:
                resultL.append(1)
            elif guessL[3] in numL:
                resultL.append(0)                  
            else:
                resultL.append('.')

   #*resultL and *guessL removes unnessasary commas and brackets in order to make the result look like in fig 2
    if(repeat==1): # checking if user entered an invalid digit and increases number of attempts if so 
        count+=1
    attemptNo+=1
    #printing the attempts - guesses - results as shown in figure 2
    print("attemptNo-",attemptNo ,"       guess-",*guessL ,"       Result-",*resultL)
    resultL.clear()
