from Questions import questions # Gets the file called questions than imports the dictionary called questions, very cool, very useful
from Other_effect import beam # Imports the beam effect from the other file, very cool, very useful
from Rain_Effect import decrypt # Imports the decrypt effect from the other file, very cool, very useful, takes a while might annoy sir :)
import random # To mix up questions WEP
import os # To check if the file exists

score = 0 # Score system determines the score of the player
hints = 3 # Hints system determines the hints the player has used
category = "" # Category is for the leaderboard

def welcome_to_awesome_quiz(): # Introduces player gives a short intro / a brief description of the categories
    beam("Welcome to the most fantastic, amazing, best crafted quiz you will ever have the joy of taking.")
    beam("This quiz will have three categories, how great is that!")
    beam("The categories are...")
    beam("General Knowledge, can you get 10 / 10?")
    beam("Sport, Hope you know lots of different sports.")
    beam("Other, it's like General Knowledge but has very random questions, so you get hints for this one. You will need it.")

def General_Knowledge():
    global category
    category = "General Knowledge"
    print("\n") # \ (if needed again) It makes a gap on the console, cleaner to look at
    beam("Welcome to the General Knowledge quiz.")
    beam("You don't get hints for this one, good luck.")
    beam("Lets get started.")
    question_getter_General(questions) # Calls the function to get the questions

def Sport():
    global category
    category = "Sport"
    print("\n") # \ (if needed again) It makes a gap on the console, cleaner to look at
    beam("Welcome to the Sport quiz.")
    beam("You don't get hints for this one, good luck.")
    beam("Lets get started.")
    question_getter_Sport(questions) # Calls the function to get the questions

def Other():
    global category
    category = "Other"
    print("\n") # \ (if needed again) It makes a gap on the console, cleaner to look at
    beam("Welcome to the most random quiz.")
    beam("For this quiz you will have 3 hints, use them wisely.")
    beam("If you need a hint, type 'hint'.")
    beam("Lets get started.")
    question_getter_Other(questions) # Calls the function to get the questions

def topic_selector(): # Asks the user for which topic they should chose
    beam("Now lets challenge you, what topic would you like to choose?")
    valid_answer = False # Needed to start the loop
    while valid_answer == False: # Simple loop to check whether the answer is one that is avaible otherwise restates the question
        beam("General Knowledge, Sport or Other ")
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
            beam("Please answer carefully")

def question_getter_General(Questions): # Grabbing the questions for the quiz # Need to change it 
    global score # Makes the score global so it can be used in the function, otherwise there would be an error, Co Pilot helped me with this
    random.shuffle(Questions) # Shuffles the questions so they are not in the same order every time
    for question in Questions: # Loops through the dictionary on other file for the stuff in questions
        if question['topic'] == "General":
            valid_answer = False
            while valid_answer == False:
                beam(question['question']) # Prints the question
                answer = input("") # Gets the answer from the player
                answer = answer.lower().strip() # Makes the answer lowercase so it can be compared to the answer in the dictionary
                if answer == "": # If the player doesn't answer the question
                    valid_answer = False
                    beam("Please answer the question not leave it blank.")
                    beam("Here's the question again.")
                elif answer in question['answer']: # Checks if the answer is correct
                    valid_answer = True
                    beam("Correct!") # If the answer is correct
                    score += 1 
                else: # If the answer is wrong
                    valid_answer = True
                    beam("Incorrect!") # Bully the player , Could change effect to make it better
                    decrypt(f"The answer is {question['answer']}.") # Tells the player the answer if they get it wrong 

def question_getter_Sport(Questions): # Grabbing the questions for the quiz # Need to change it 
    global score # Makes the score global so it can be used in the function, otherwise there would be an error, Co Pilot helped me with this
    random.shuffle(Questions) # Shuffles the questions so they are not in the same order every time
    for question in Questions: # Loops through the dictionary on other file for the stuff in questions
        if question['topic'] == "Sport":
            valid_answer = False
            while valid_answer == False:
                beam(question['question']) # Prints the question
                answer = input("") # Gets the answer from the player
                answer = answer.lower().strip() # Makes the answer lowercase so it can be compared to the answer in the dictionary
                if answer == "":
                    valid_answer = False
                    beam("Please answer the question not leave it blank.")
                    beam("Here's the question again.")
                elif answer in question['answer']: # Checks if the answer is correct
                    valid_answer = True
                    beam("Correct!") # If the answer is correct,
                    score += 1 
                else:
                    valid_answer = True
                    beam("Incorrect!")
                    decrypt(f"The answer is {question['answer']}.") # Tells the player the answer if they get it wrong
           
def question_getter_Other(Questions): # Grabbing the questions for the quiz # Need to change it 
    global score # Makes the score global so it can be used in the function, otherwise there would be an error, Co Pilot helped me with this
    global hints # Makes the hints global so it can be used in the function, otherwise there would be an error, Co Pilot helped me with this
    random.shuffle(Questions) # Shuffles the questions so they are not in the same order every time
    for question in Questions: # Loops through the dictionary on other file for the stuff in questions
        if question['topic'] == "Other":
            hint_loop = True # Only idea for hints to work
            while hint_loop == True: # Simple loop 
                beam(question['question']) # Prints the question
                answer = input("") # Gets the answer from the player
                answer = answer.lower().strip() # Makes the answer lowercase so it can be compared to the answer in the dictionary, strip makes it so spaces after the answer don't matter
                if answer == "":
                    hint_loop = True
                    beam("Please answer the question.")
                elif answer in question['answer']: # Checks if the answer is correct
                    hint_loop = False # Ends the loop as it is an answer available
                    beam("Correct!") # If the answer is correct
                    score += 1 
                elif answer == "hint" and hints > 0: # If the player types hint, it will give them a hint
                    hint_loop = True
                    beam(question['hint'])
                    hints -= 1
                    beam(f"You have {hints} hints left.")
                    beam("Here's the question again.")
                elif answer == "hint" and hints == 0: # If the player types hint, it will give them a hint
                    hint_loop = True
                    beam("You have no hints left.")
                    beam("Please answer the question.")
                else:
                    hint_loop = False
                    beam("Incorrect!")
                    decrypt(f"The answer is {question['answer']}.") # Tells the player the answer if they get it wrong

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
                    decrypt(f"Highest Score in {category}: {line.strip()}")
                    return
            beam(f"No scores yet in {category}.")
    else:
        beam("No scores yet.")

#########################################################################################################################

def main(): # Sir won't let the large 1000 line code happen :( wants it to be neat, make it condensed into large function
    global score
    global hints
    global category
    welcome_to_awesome_quiz() # Calls the welcome function to introduce player etc
    topic_selector()
    beam(f"Your score in this quiz is: {score} / 10" ) # Prints the score of the player
    beam("Would you like to see the percentage of your score? (Yes / No)") # Asks the player if they would like to see the percentage of their score
    valid_answer = False # Needed to start the loop
    while valid_answer == False: # Simple loop to check whether the answer is one that is avaible otherwise restates the question
        answer = input("") # Gets the answer from the player
        answer = answer.lower().strip() # Makes the answer lowercase
        if answer == "yes": # Checks if the answer is either yes or no
            valid_answer = True # Ends the loop
            percentage = (score / 10) * 100 # Calculates the percentage of the score
            beam(f"Your score is {percentage}%") # Prints the percentage of the score
        elif answer == "no":
            valid_answer = True
            beam("Okay, moving on.")
        else:
            valid_answer = False
            beam("Please answer carefully")
    beam("What is your name?")
    player_name = input("").strip()
    update_leaderboard(player_name, score, category)
    display_leaderboard(category)
    beam("Would you like to play again? (Yes / No)") # Asks the player if they would like to play again
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
            beam("Thank you for playing")
        else:
            beam("Please answer carefully")

main() # Calls the final main program and makes stuff happen