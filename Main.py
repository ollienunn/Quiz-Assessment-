from Questions import questions # Gets the file called questions than imports the dictionary called questions, very cool, very useful
import sys # Random stuff to make typewritter effect work
from time import sleep # Kinda understand this 
import random # To mix up questions WEP

score = 0 # Score system determines the score of the player
hints = 3 # Hints system determines the hints the player has used

def typewritter(words): # Typewritter effect to make the quiz look less boring
    for char in words:
        sleep(0.03) # Change this for the typewritter speed
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in '.!?':
            sleep(0.5)
    sys.stdout.write("\n") # Adds a gap between the next line

#typewritter("Your gonna love this quiz.") # Have to start with 'typewritter' for it to work

def welcome_to_awesome_quiz(): # Introduces player gives a short intro / a brief description of the categories
    typewritter("Welcome sir to the most fantastic, amazing, best crafted quiz you will ever have the joy of taking.")
    typewritter("This quiz will have three categories, how great is that!")
    typewritter("The categories are...")
    typewritter("General Knowledge, can you get 10 / 10?")
    typewritter("Sport, Hope you know lots of different sports.")
    typewritter("Other, it's like General Knowledge but has very random questions, so you get hints for this one. You will need it.")

#########################################################################################################################

#Could make this a lot cleaner, will do later, for now make sure it works

def General_Knowledge():
    print("\n") # \ (if needed again) It makes a gap on the console, cleaner to look at
    typewritter("Welcome to the General Knowledge quiz")
    typewritter("Lets get started")
    question_getter_General(questions) # Calls the function to get the questions

def Sport():
    print("\n") # \ (if needed again) It makes a gap on the console, cleaner to look at
    typewritter("Welcome to the Sport quiz")
    typewritter("Lets get started")
    question_getter_Sport(questions) # Calls the function to get the questions

def Other():
    print("\n") # \ (if needed again) It makes a gap on the console, cleaner to look at
    typewritter("Welcome to the most random quiz")
    typewritter("For this quiz you will have 3 hints, use them wisely")
    typewritter("Lets get started")
    question_getter_Other(questions) # Calls the function to get the questions

#########################################################################################################################

def topic_selector(): # Asks the user for which topic they should chose
    typewritter("Now lets challenge you, what topic would you like to choose?")
    valid_answer = False # Needed to start the loop
    while valid_answer == False: # Simple loop to check whether the answer is one that is avaible otherwise restates the question
        typewritter("General Knowledge, Sport or Other ")
        decision = input("") # Gets the input from the player
        decision_real = decision.lower() # Makes it all lowercase so any way to type it will work
        if decision_real == "general knowledge": # Must be all lower case
            valid_answer = True # Ends the loop as it is an answer available
            General_Knowledge() # Moves to the General knowledge part
        elif decision_real == "sport":
            valid_answer = True
            Sport() # Moves to the Sport part
        elif decision_real == "other":
            valid_answer = True
            Other() # Moves to the Other part
        else:
            print("Please answer carefully")

#########################################################################################################################
#Could make this a lot cleaner will do later, for now make sure it works

def question_getter_General(Questions): # Grabbing the questions for the quiz # Need to change it 
    global score # Makes the score global so it can be used in the function, otherwise there would be an error, Co Pilot helped me with this
    random.shuffle(Questions) # Shuffles the questions so they are not in the same order every time
    for question in Questions: # Loops through the dictionary on other file for the stuff in questions
        if question['topic'] == "General":
            typewritter(question['question']) # Prints the question
            answer = input("") # Gets the answer from the player
            answer = answer.lower().strip() # Makes the answer lowercase so it can be compared to the answer in the dictionary
            if answer in question['answer']: # Checks if the answer is correct
                typewritter("Correct!") # If the answer is correct, Early stages of the quiz, will change and add score system later
                score += 1 
            else: # If the answer is wrong
                typewritter("Incorrect!") # Bully the player
                typewritter(f"The answer is {question['answer']}") # Tells the player the answer if they get it wrong

def question_getter_Sport(Questions): # Grabbing the questions for the quiz # Need to change it 
    global score # Makes the score global so it can be used in the function, otherwise there would be an error, Co Pilot helped me with this
    random.shuffle(Questions) # Shuffles the questions so they are not in the same order every time
    for question in Questions: # Loops through the dictionary on other file for the stuff in questions
        if question['topic'] == "Sport":
            typewritter(question['question']) # Prints the question
            answer = input("") # Gets the answer from the player
            answer = answer.lower().strip() # Makes the answer lowercase so it can be compared to the answer in the dictionary
            if answer in question['answer']: # Checks if the answer is correct
                typewritter("Correct!") # If the answer is correct, Early stages of the quiz, will change and add score system later
                score += 1 
            else:
                typewritter("Incorrect!")
                typewritter(f"The answer is {question['answer']}") # Tells the player the answer if they get it wrong

def question_getter_Other(Questions): # Grabbing the questions for the quiz # Need to change it 
    global score # Makes the score global so it can be used in the function, otherwise there would be an error, Co Pilot helped me with this
    global hints # Makes the hints global so it can be used in the function, otherwise there would be an error, Co Pilot helped me with this
    random.shuffle(Questions) # Shuffles the questions so they are not in the same order every time
    for question in Questions: # Loops through the dictionary on other file for the stuff in questions
        if question['topic'] == "Other":
            hint_loop = True # Only idea for hints to work
            while hint_loop == True: # Simple loop 
                typewritter(question['question']) # Prints the question
                answer = input("") # Gets the answer from the player
                answer = answer.lower().strip() # Makes the answer lowercase so it can be compared to the answer in the dictionary, strip makes it so spaces after the answer don't matter
                if answer == "":
                    hint_loop = True
                    typewritter("Please answer the question")
                elif answer in question['answer']: # Checks if the answer is correct
                    hint_loop = False # Ends the loop as it is an answer available
                    typewritter("Correct!") # If the answer is correct, Early stages of the quiz, will change and add score system later
                    score += 1 
                elif answer == "hint" and hints > 0: # If the player types hint, it will give them a hint
                    hint_loop = True
                    typewritter(question['hint'])
                    hints -= 1
                    typewritter(f"You have {hints} hints left")
                    typewritter("Here's the question again")
                elif answer == "hint" and hints == 0: # If the player types hint, it will give them a hint
                    hint_loop = True
                    typewritter("You have no hints left")
                    typewritter("Please answer the question")
                else:
                    hint_loop = False
                    typewritter("Incorrect!")
                    typewritter(f"The answer is {question['answer']}") # Tells the player the answer if they get it wrong
#########################################################################################################################

def main(): # Sir won't let the large 1000 line code happen :( wants it to be neat, make it condensed into large function
    #welcome_to_awesome_quiz() # Calls the welcome function to introduce player etc
    global score
    global hints
    topic_selector()
    typewritter(f"Your score in this quiz is: {score}" ) # Prints the score of the player
    typewritter("Would you like to play again?") # Asks the player if they would like to play again
    # Loop to make sure the player answers yes or no otherwise it will keep asking the question
    valid_answer = False # Needed to start the loop
    while valid_answer == False: # Simple loop to check whether the answer is one that is avaible otherwise restates the question
        answer = input("") # Gets the answer from the player
        answer = answer.lower() # Makes the answer lowercase
        if answer == "yes": # Checks if the answer is either yes or no
            valid_answer = True # Ends the loop as it is an answer available
            score = 0
            hints = 3
            main()
        elif answer == "no":
            valid_answer = True
            typewritter("Thank you for playing")
        else:
            print("Please answer carefully")
    
    #question_getter(questions) # Not sure what to do with him probably will be used in something else

main() # Calls the final main program and makes stuff happen