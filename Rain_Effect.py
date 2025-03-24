from terminaltexteffects.effects.effect_rain import Rain

def rain(text):
    effect = Rain(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

text =("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO" * 10 + "\n") * 10
rain(text)