from terminaltexteffects.effects.effect_print import Print
from time import sleep

def beam(text):
    effect = Print(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
            