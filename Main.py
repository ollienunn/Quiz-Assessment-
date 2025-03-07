from Questions import questions # Gets the file called questions than imports the dictionary called questions, very cool, very useful

# The main source of code and file
def welcome_to_awesome_quiz(): # Introduces player gives a short intro
    print("Welcome sir the most fantastic amazing quiz you will ever participate")
    print("This quiz will have three categories, how great is that")

def question_getter(Questions): # Grabbing the questions for the quiz
    for questions in Questions:
        print(f"The topic is {questions['topic']}")

def main(): # Sir won't let the large 1000 line code happen :( wants it to be neat, make it condensed into large function
    welcome_to_awesome_quiz() # Calls the welcome function to introduce player etc
    question_getter(questions)







main() # Calls the final main program and makes stuff happen