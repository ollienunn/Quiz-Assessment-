from Questions import questions # Gets the file called questions than imports the dictionary called questions, very cool, very useful
import sys # Random stuff to make typewritter effect work
from time import sleep # Kinda understand this 
#import random # To mix up questions WEP

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
    typewritter("The categories are....")
    typewritter("General Knowledge, can you get 10 / 10?")
    typewritter("Sport, Hope you know lots of different sports.")
    typewritter("Other, it's like General Knowledge but has very random questions, so you get hints for this one. You will need it.")

def topic_selector(): # Asks the user for which topic they should chose
    typewritter("Now lets challenge you, what topic would you like to choose?")
    valid_answer = False # Needed to start the loop
    while valid_answer == False: # Simple loop to check whether the answer is one that is avaible otherwise restates the question
        typewritter("General Knowledge, Sport or Other ")
        decision = input("") # Gets the input from the player
        decision_real = decision.lower() # Makes it all lowercase so any way to type it will work
        if decision_real == "general knowledge": # Must be all lower case
            valid_answer = True # Ends the loop as it is an answer available
            typewritter("Good choice on General Knowledge")
        elif decision_real == "sport":
            valid_answer = True
            typewritter("So your sporty")
        elif decision_real == "other":
            valid_answer = True
            typewritter("Hope your prepared")
        else:
            print("Please answer carefully")

def question_getter(Questions): # Grabbing the questions for the quiz # Need to change it 
    for questions in Questions: # Loops through the dictionary on other file for the stuff in questions
        typewritter(f"The topic is {questions['topic']}")# Just a test not definate

def main(): # Sir won't let the large 1000 line code happen :( wants it to be neat, make it condensed into large function
    welcome_to_awesome_quiz() # Calls the welcome function to introduce player etc
    topic_selector()
    
    #question_getter(questions) # Not sure what to do with him






main() # Calls the final main program and makes stuff happen