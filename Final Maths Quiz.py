# Main method starts at line 194 press cmd + j to select
def openFile (fileName):
            # Open file and put data into classData list
            classData = []
            try:
                        myFile = open(fileName+'.txt', 'rt')
                        for line in myFile:
                                    quizResults = line.strip()                                   
                                    try:
                                                evaluatedQuizResults = eval(quizResults)
                                                for i in range (1,4):
                                                            evaluatedQuizResults[i] = int(evaluatedQuizResults[i])
                                                print(evaluatedQuizResults)
                                                classData.append(evaluatedQuizResults)

                                    except TypeError:
                                                print ("There was an error importing the data")
                                                print ("Is the data in the correct format?")
                                    
                        myFile.close()
                        fileLoadedSuccessfully = True
                        return fileLoadedSuccessfully, classData
            except OSError:
                        print ("File not found.")
                        print ("Make sure the file exists.")
            
def newFile (fileName):
            #Gets file name and make new file with 1 item in the list
            #Use openFile function to load the file and adds example to classData
            print ("this will open a new file and add an item into the list")
            myFile = open (fileName + ".txt", 'a')
            myFile.write (str(["example",0,0,0,0,0,0]))
            myFile.close()
            flagAndData = openFile(fileName)
            return flagAndData
            
def viewData (classData):
            # Simply shows the data thats loaded into classData                        
            studentNo = 1 #Probably not needed
            # Print the data in classData to screen
            # If the passed data has already been sorted than this is displayed avoiding duplication of code.
            for innerlist in classData:
                        print (str(studentNo) + " " + str(innerlist))
                        studentNo+= 1
            print ("Class Details Printed!!")
def addRecord ():
            # Enter a new record but don't save until user requests
            user = ["Name",1,2,3,4,5,6] # Assign here should clear results and is probably needed
            #myFile = open('classA.txt', 'a') #not sure if needed
            user [0] = input("Enter your name to add for the list ") #Do this directly to class data making code more efficient
            try:
                        user [1] = input("Enter your quiz1. ") 
                        user [2] = input("Enter your quiz2. ")
                        user [3] = input("Enter yourb quiz3. " )
                        user [4] = 0
                        user [5] = 0
                        user [6] = 0
            except ValueError:
                        print ("Please enter a name and then quiz scores from 1-10.")                      
            classData.append (user)

def deleteRecord ():
            #b. pass in userPupilChoice
            # Allows user to delete a record.
            userPupilChoice =  int(input("Type the row number of the student that you would like to delete. ")) - 1 #Add type handling
            del classData[userPupilChoice]

def editRecord ():
            # While prevents continuation if no user is selected
            while True:
                        try:
                                    userPupilChoice =  int(input("Select the number of the row to edit the user. ")) - 1
                                    break
                        except ValueError:
                                    print("Please enter a valid option from the list.")
                                    
            try:
                        classData[userPupilChoice][0] = str(input("Enter the new name. ")) # Add type handling
            # TODO: simple for loop for adding quiz data with a try except for type
            except ValueError:
                        print("There was a problem with the name entered.  The name of this student will stay the same.")
            tempQuizScore = ['0','0','0','0']

            for i in range(1,4):
                        # Would be better without the temporary list but it defaults to 0 otherwise.
                        tempQuizScore [i] = classData[userPupilChoice][i]                       
                        
                        try:
                                    classData[userPupilChoice][i] = int(input("Enter the quiz result for test " + str(i) + ". ")) # Add type handling
                        except ValueError:
                                     print("There was a problem with your quiz score edit.  The score for quiz " + str(i) + " will remain the same.")
                                     classData[userPupilChoice][i] =  tempQuizScore [i]
                                     
def saveFile (fileName):
            # Save as?
            # Open for writing to remove contents of file.
            try:
                        myFile = open(fileName+'.txt', 'wt')
                        myFile.close()
                        # Open for reading and write classData list to file.
                        myFile = open(fileName+'.txt','a')                        
                        for innerlist in classData:
                                    inList = str(innerlist)
                                    myFile.write(inList + "\n")
                        myFile.close()
            except OSError:
                        print ("File not found.")
                        print ("Make sure the file exists.")
def takeQuiz ():
                        # implement quiz
            
            userPupilChoice =  int(input()) -1  #Add type handling
            import random
            # Welcome text
            print ("Welcome to the Arithmatic Quiz.")
            ##                        name1 = input("What is your name")
            print (userPupilChoice)
            print ("Welcome" + " " + str(classData[userPupilChoice][0]))
            quizScore = 0

            # Quiz for loop with random numbers
            for i in range(0,3):
                        # Generate numbers and operators
                        a = random.randint(1,12)
                        b= random.randint(1,12)
                        randChooseOperator = random.randint(0,2)
                        correctAnswer = [a + b,a-b,a*b]
                        operator = ["+","-","x"]

                        # Assemble the question from these components
                        print("Question " + str(i+1))
                        print (correctAnswer[randChooseOperator])
                        while True:
                                    try:
                                                userAnswer = int(input("What is " + str(a) + operator[randChooseOperator] + str(b) + "? "))
                                                break
                                    except ValueError:
                                                print("Please enter a whole number.")

                        # Check the answer
                        if userAnswer == correctAnswer[randChooseOperator]:
                                    print ("Correct")
                                    quizScore += 1
                        else:
                                    print(userAnswer)
                                    print ("Incorrect")
                                    
                        # Feedback score
            print("Your score was " + str(quizScore))
            scrWasAdded = False
            for i in range (1,4):
                        print (classData[userPupilChoice])
                        print("iteration no " + str(i))
                        if int(classData[userPupilChoice][i]) <= 0 and scrWasAdded == False:
                                    print (str(classData[userPupilChoice][i]) + "is less than or equal to 0")
                                    classData[userPupilChoice][i] = quizScore
                                    scrWasAdded = True
                                    print ("quiz score added to " + classData[userPupilChoice][0] + "Quiz " + str(i))
                        # If the score wasn't added already and there are already 3 scores recorded
                        # the previous scores are moved and the earliest score is discarded.
            if int(classData[userPupilChoice][3]) > 0 and scrWasAdded == False:
                        classData[userPupilChoice][1] = classData[userPupilChoice][2]
                        classData[userPupilChoice][2] = classData[userPupilChoice][3]
                        classData[userPupilChoice][3] = quizScore

def sortData (classData):
            print("Which field would you like to sort on?")
            print("1. Student Name")
            print("2. Quiz 1")
            print("3. Quiz 2")
            print("4. Quiz 3")
            print("5. Total Score")
            print("6. Average Score")
            print("7. Highest Score")
            sortedClassData = [] 
            try:
                        sortedFieldRequest = int(input())
                        
                        sortedClassData = sorted(classData, key=lambda classData: classData[sortedFieldRequest - 1])
                        
            except ValueError:
                        print ("Whoops! this option isn't in the list. ")
                        print (" Please enter a number from 1 to 7.")
                        print ("Your data could not be sorted.")
                        sortedClassData = classData
            return sortedClassData


def calculateStats ():
            user = ["Name" , 1, 2, 3, 4, 5, 6]

            for innerlist in classData:
                        user[0] = innerlist[0]
                        for i in range (1, 3):
                                    user[i] = int(innerlist[i])
                        innerlist = user
                        innerlist[4] = int(innerlist[1]) + int(innerlist[2]) +int(innerlist[3])
                        innerlist[5] = round(int(innerlist[4])/3,1)
                        biggest = 0
                        for i in range (1,4):
                                    if int(innerlist[i]) > int(biggest):
                                                biggest = int(innerlist[i])
                        innerlist[6] = biggest

 # Main Method                                   
classData = []
optionChoice = ""
fileLoaded = False
print ("Welcome to the Arithmatic Quiz")

while optionChoice != "x" and fileLoaded == False:

            print ("What would you like to do?")
            print ("1. Load file?")
            print ("2. Create a new file")
            print ("x. Exit program")
            optionChoice = input()
            if optionChoice == "1":
                        
                        requestedFileName = input("Which class file would you like to open?")
                        # returns the updated flag followfolloweded by the classdata from the file
                        fileLoaded, classData = openFile(requestedFileName)

            elif optionChoice == "2":
                         print ("A new file will be created")
                         requestedFileName = input("What is the name of the file you would like to create?")
                         fileLoaded, classData = newFile(requestedFileName)

                        
while optionChoice !="x":
            print ("Welcome to the Arithmatic Quiz")
            print ("What would you like to do?")
            print ("1. Load a different file.")
            print ("2. Create a new file.")
            print ("3. Take a quiz.")
            print ("4. Edit student data.")
            print ("5. View info on class.")
            print ("x. Exit program.")
            optionChoice = input()
            if optionChoice == "1":
                        requestedFileName = input("Which class file would you like to open?")
            # returns the updated flag followed by the classdata from the loaded file
                        fileLoaded, classData = openFile(requestedFileName)
                                    
            if optionChoice == "2":
                        print ("A new file will be created")
                        requestedFileName = input("Which class file would you like to open?")
                        fileLoaded, classData = newFile(requestedFileName)
            if optionChoice == "3":
                        print("Select the user number of the student who is taking the quiz.")
                        viewData(classData)
                        takeQuiz()
                        saveChangeChoice = input("Would you like to save the changes?")
                        if saveChangeChoice == "y" or "Y":
                                    saveFile(requestedFileName)
            if optionChoice == "4":
                        # give sub options to add edit and delete records offer the choice to save data once edited.
                        subOptionChoice = ""
                        editAgain = "y"
                        while editAgain == "y":
                                    print ("How would you like to edit the class data?")
                                    print ("a. Add a record. ")
                                    print ("b. Edit a record. ")
                                    print("c. Delete a record. ")
                                    subOptionChoice = input()
                                    if subOptionChoice == "a":
                                                addRecord()
                                                print("Please see the updated class data below. ")
                                                calculateStats()
                                                viewData(classData)
                                                
                                    elif subOptionChoice == "b":
                                                viewData(classData)
                                                editRecord()
                                                print("Please see the updated class data below. ")
                                                calculateStats()
                                                viewData(classData)
                                                saveChangeChoice = input("Would you like to save the changes?")
                                                if saveChangeChoice == "y" or "Y":
                                                            saveFile(requestedFileName)
                                                                                                                                               
                                    elif subOptionChoice == "c":
                                                viewData(classData)
                                                deleteRecord()
                                                print("Please see the updated class data below. ")
                                                viewData(classData)
                                    else:
                                                print("Whoops! That wasn't an option from the list")
                                    editAgain = input("Would you like to edit more student data? (y/n)")
                                    
            if optionChoice == "5":
                        viewAgain = "y"
                        while viewAgain == "y":
                                    calculateStats()
                                    print ("What would you like to do?")
                                    print ("a. View data as saved to file?")
                                    print ("b. Sort and view data?")
                                    subOptionChoice = ""
                                    subOptionChoice = input ()
                                    if subOptionChoice == "a":
                                                viewData(classData)
                                    elif subOptionChoice == "b":
                                                sortedClassData = sortData(classData)
                                                viewData(sortedClassData)
                                                            
                                    else:
                                                print("Whoops! That wasn't an option from the list")
                                    viewAgain = input("Would you like to view again? (y/n)")

                        

