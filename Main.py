from Questions import questions # Gets the file called questions than imports the dictionary called questions, very cool, very useful
import sys # Random stuff to make typewritter effect work
from time import sleep # Kinda understand this 
import random # To mix up questions WEP
import os # To check if the file exists

score = 0 # Score system determines the score of the player
hints = 3 # Hints system determines the hints the player has used
category = "" # Category is for the leaderboard

def typewritter(words): # Typewritter effect to make the quiz look less boring
    for char in words:
        sleep(0.03) # Change this for the typewritter speed
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in '.!?':
            sleep(0.5)
    sys.stdout.write("\n") # Adds a gap between the next line

def welcome_to_awesome_quiz(): # Introduces player gives a short intro / a brief description of the categories
    typewritter("Welcome to the most fantastic, amazing, best crafted quiz you will ever have the joy of taking.")
    typewritter("This quiz will have three categories, how great is that!")
    typewritter("The categories are...")
    typewritter("General Knowledge, can you get 10 / 10?")
    typewritter("Sport, Hope you know lots of different sports.")
    typewritter("Other, it's like General Knowledge but has very random questions, so you get hints for this one. You will need it.")


def General_Knowledge():
    global category
    category = "General Knowledge"
    print("\n") # \ (if needed again) It makes a gap on the console, cleaner to look at
    typewritter("Welcome to the General Knowledge quiz.")
    typewritter("You don't get hints for this one, good luck.")
    typewritter("Lets get started.")
    question_getter_General(questions) # Calls the function to get the questions

def Sport():
    global category
    category = "Sport"
    print("\n") # \ (if needed again) It makes a gap on the console, cleaner to look at
    typewritter("Welcome to the Sport quiz.")
    typewritter("You don't get hints for this one, good luck.")
    typewritter("Lets get started.")
    question_getter_Sport(questions) # Calls the function to get the questions

def Other():
    global category
    category = "Other"
    print("\n") # \ (if needed again) It makes a gap on the console, cleaner to look at
    typewritter("Welcome to the most random quiz.")
    typewritter("For this quiz you will have 3 hints, use them wisely.")
    typewritter("If you need a hint, type 'hint'.")
    typewritter("Lets get started.")
    question_getter_Other(questions) # Calls the function to get the questions

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


def question_getter_General(Questions): # Grabbing the questions for the quiz # Need to change it 
    global score # Makes the score global so it can be used in the function, otherwise there would be an error, Co Pilot helped me with this
    random.shuffle(Questions) # Shuffles the questions so they are not in the same order every time
    for question in Questions: # Loops through the dictionary on other file for the stuff in questions
        if question['topic'] == "General":
            valid_answer = False
            while valid_answer == False:
                typewritter(question['question']) # Prints the question
                answer = input("") # Gets the answer from the player
                answer = answer.lower().strip() # Makes the answer lowercase so it can be compared to the answer in the dictionary
                if answer == "": # If the player doesn't answer the question
                    valid_answer = False
                    typewritter("Please answer the question not leave it blank.")
                    typewritter("Here's the question again.")
                elif answer in question['answer']: # Checks if the answer is correct
                    valid_answer = True
                    typewritter("Correct!") # If the answer is correct
                    score += 1 
                else: # If the answer is wrong
                    valid_answer = True
                    typewritter("Incorrect!") # Bully the player
                    typewritter(f"The answer is {question['answer']}.") # Tells the player the answer if they get it wrong 

def question_getter_Sport(Questions): # Grabbing the questions for the quiz # Need to change it 
    global score # Makes the score global so it can be used in the function, otherwise there would be an error, Co Pilot helped me with this
    random.shuffle(Questions) # Shuffles the questions so they are not in the same order every time
    for question in Questions: # Loops through the dictionary on other file for the stuff in questions
        if question['topic'] == "Sport":
            valid_answer = False
            while valid_answer == False:
                typewritter(question['question']) # Prints the question
                answer = input("") # Gets the answer from the player
                answer = answer.lower().strip() # Makes the answer lowercase so it can be compared to the answer in the dictionary
                if answer == "":
                    valid_answer = False
                    typewritter("Please answer the question not leave it blank.")
                    typewritter("Here's the question again.")
                elif answer in question['answer']: # Checks if the answer is correct
                    valid_answer = True
                    typewritter("Correct!") # If the answer is correct,
                    score += 1 
                else:
                    valid_answer = True
                    typewritter("Incorrect!")
                    typewritter(f"The answer is {question['answer']}.") # Tells the player the answer if they get it wrong
           
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
                    typewritter("Please answer the question.")
                elif answer in question['answer']: # Checks if the answer is correct
                    hint_loop = False # Ends the loop as it is an answer available
                    typewritter("Correct!") # If the answer is correct
                    score += 1 
                elif answer == "hint" and hints > 0: # If the player types hint, it will give them a hint
                    hint_loop = True
                    typewritter(question['hint'])
                    hints -= 1
                    typewritter(f"You have {hints} hints left.")
                    typewritter("Here's the question again.")
                elif answer == "hint" and hints == 0: # If the player types hint, it will give them a hint
                    hint_loop = True
                    typewritter("You have no hints left.")
                    typewritter("Please answer the question.")
                else:
                    hint_loop = False
                    typewritter("Incorrect!")
                    typewritter(f"The answer is {question['answer']}.") # Tells the player the answer if they get it wrong

#########################################################################################################################

# My idea and i tried to do it but co pilot carried me, this is for the leaderboard stuff
# Didn't understand how to do it all co pilot, can hashtag out and not use in the marking
def update_leaderboard(player_name, score, category):
    leaderboard_file = "leaderboard"
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r") as file:
            lines = file.readlines()
            highest_score = 0
            new_lines = []
            updated = False
            for line in lines:
                if category in line:
                    highest_score = int(line.strip().split(" with ")[1].split(" ")[0])
                    if score > highest_score:
                        new_lines.append(f"{player_name} with {score} in {category}\n")
                        updated = True
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)
            if not updated:
                new_lines.append(f"{player_name} with {score} in {category}\n")
            with open(leaderboard_file, "w") as file:
                file.writelines(new_lines)
    else:
        with open(leaderboard_file, "w") as file:
            file.write(f"{player_name} with {score}\n") #in {category}

def display_leaderboard(category):
    leaderboard_file = "leaderboard"
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                if category in line:
                    typewritter(f"Highest Score in {category}: {line.strip()}")
                    return
            typewritter(f"No scores yet in {category}.")
    else:
        typewritter("No scores yet.")

#########################################################################################################################

def main(): # Sir won't let the large 1000 line code happen :( wants it to be neat, make it condensed into large function
    global score
    global hints
    global category
    #welcome_to_awesome_quiz() # Calls the welcome function to introduce player etc
    topic_selector()
    typewritter(f"Your score in this quiz is: {score}" ) # Prints the score of the player
    typewritter("Can we get your name please? ")
    player_name = input("").strip()
    update_leaderboard(player_name, score, category)
    display_leaderboard(category)
    typewritter("Would you like to play again?") # Asks the player if they would like to play again
    # Loop to make sure the player answers yes or no otherwise it will keep asking the question
    valid_answer = False # Needed to start the loop
    while valid_answer == False: # Simple loop to check whether the answer is one that is avaible otherwise restates the question
        answer = input("") # Gets the answer from the player
        answer = answer.lower().strip() # Makes the answer lowercase
        if answer == "yes": # Checks if the answer is either yes or no
            valid_answer = True # Ends the loop as it is an answer available
            score = 0
            hints = 3
            category = "" # Resets category
            main()
        elif answer == "no":
            valid_answer = True
            typewritter("Thank you for playing")
        else:
            print("Please answer carefully")

main() # Calls the final main program and makes stuff happen