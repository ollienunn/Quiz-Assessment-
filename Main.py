from Questions import questions # Gets the file called questions than imports the dictionary called questions, very cool, very useful
import sys # Random stuff to make typewritter effect work
from time import sleep # Kinda understand this 

def typewritter(words): # Typewritter effect to make the quiz look less boring
    for char in words:
        sleep(0.03) # Change this for the typewritter speed
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in '.!?':
            sleep(0.5)
    sys.stdout.write("\n") # Adds a gap between the next line

#typewritter("Youe iwehfowihf.") # Have to start with 'typewritter' for it to work

def welcome_to_awesome_quiz(): # Introduces player gives a short intro
    typewritter("Welcome sir the most fantastic amazing quiz you will ever participate")
    typewritter("This quiz will have three categories, how great is that")

def question_getter(Questions): # Grabbing the questions for the quiz
    for questions in Questions: # Loops through the dictionary on other file for the stuff in questions
        print(f"The topic is {questions['topic']}")# Just a test not definate



def main(): # Sir won't let the large 1000 line code happen :( wants it to be neat, make it condensed into large function
    welcome_to_awesome_quiz() # Calls the welcome function to introduce player etc
    question_getter(questions)







main() # Calls the final main program and makes stuff happen