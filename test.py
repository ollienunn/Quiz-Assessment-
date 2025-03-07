import sys
from time import sleep

def typewritter(words):
    for char in words:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in '.!?':
            sleep(0.5)
    sys.stdout.write("\n")

typewritter("Youe iwehfowihf.")
