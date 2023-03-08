class Animal:

    m_name = ""
    m_questions = list()

    def __init__(self, name):
        
        self.m_name = name

    def AddNewQuestion(self, question):

        self.m_questions.append(question)

class ValueOutOfRange(Exception):
    #This class is for triggering a custom exception
    pass
        
def RunMenu(menuList):

    continueLoop = True
    while continueLoop == True:

        try: #Tells the compiler to attempt the code indented, passing to an exception if an error occurs
            
            #Start text to the screen with the initial value in the passed list
            print(menuList[0])

            for x in range(1, len(menuList)): #Loops from 1 (because be have used index 0 already), until the end of the indexes in our passed list
                print(str(x) + ": " + menuList[x]) #Prints out a formatted text screen, using the text passed up to the function inside the list, using x as the index counter

            menuChoice = int(input("\nPlease make a selection from the list provided:\n")) #Requests the user enter an int - then saves it into the variable assignment

            if menuChoice > len(menuList) - 1 or menuChoice < 1:
                raise ValueOutOfRange #Raises the custom exception if the IF statement validates as TRUE

        except ValueOutOfRange: #Triggers when the user enters a value outside of the list range provided

            print("\n\nError! PLease only enter a number from the list indicated, please try again...")
            input("[Press Enter to Try Again]\n\n")

        except ValueError: #Triggers when the user enters a non-integer value

            print("\n\nError! PLease only enter a valid whole number, please try again...")
            input("[Press Enter to Try Again]\n\n")

        except: #Triggers exception - no specific condition required.

            print("\n\nError! An unknown bug as occurred, please try again...")
            input("[Press Enter to Try Again]\n\n")

        else: #Triggers only when no exception has been raised!

            continueLoop = False
            return menuChoice #Returns the user's input

def ProgramStarter(guessedAnimals):

    print("\nPlease think of an animal...")
    input("When you are ready, please press enter to begin...\n\n")
    animalName = input("\nPlease enter the name of your first animal: \n")
    guessedAnimals.append(Animal(animalName))
    animalQuestion = input("\nPlease enter a question which answer could be for a " + guessedAnimals[0].m_name + ": \n")
    guessedAnimals[0].m_questions.append(animalQuestion)

    return guessedAnimals

def MakeAGuess(guessedAnimals):

    print("\nPlease think of an animal...")
    input("When you are ready, please press enter to begin...\n\n")

    for x in range(0, len(guessedAnimals)):

        for y in range(0, len(guessedAnimals[x].m_questions)):

            menuList = ["\n" + guessedAnimals[x].m_questions[y], "Yes", "No"]
            menuChoice = RunMenu(menuList)

            if menuChoice == 1:
                                
                menuList = ["Is your animal a " + guessedAnimals[x].m_name, "Yes", "No"]
                menuChoice = RunMenu(menuList)

                if menuChoice == 2:

            

    return guessedAnimals

def Main():
    
    guessedAnimals = list()
    continueLoop = True
    while continueLoop == True:
        
        print("----------Guessing Game-----------")
        
        if len(guessedAnimals) == 0:

            menuChoice = ["What would you like to do?", "Start the program", "Exit"]
            choice = RunMenu(menuChoice)
            
            if choice == 1:
                guessedAnimals = ProgramStarter(guessedAnimals)
            else:
                continueLoop = False

        else:

            menuChoice = ["What would you like to do?", "Guess my Animal", "Exit"]
            choice = RunMenu(menuChoice)
            
            if choice == 1:
                guessedAnimals = MakeAGuess(guessedAnimals)
            else:
                continueLoop = False
                

    
    

#----------------------Code Runs from this point down---------------------------------------------------------------------------

Main()

