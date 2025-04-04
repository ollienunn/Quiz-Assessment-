from terminaltexteffects.effects.effect_decrypt import Decrypt

def decrypt(text):
    effect = Decrypt(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)