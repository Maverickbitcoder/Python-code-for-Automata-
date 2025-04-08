"""
1.	Must start with a digit (0-9).
2.	Can have any number of lowercase or uppercase letters in the middle.
3.	Must have at least one underscore _ somewhere after the letters.
4.	Must end with a capital letter.
5.	Minimum length of 5 characters.
"""

from graphviz import Digraph

class DigitStartPasswordDFA:
    def __init__(self):
        self.states = {'start', 'digit', 'letters', 'underscore', 'final_cap'}
        self.final_states = {'final_cap'}
        self.start_state = 'start'

    def accepts(self, password):
        if len(password) < 5:
            return False

        current_state = self.start_state
        seen_underscore = False

        for i, char in enumerate(password):
            if current_state == 'start':
                if char.isdigit():
                    current_state = 'digit'
                else:
                    return False

            elif current_state == 'digit':
                if char.isalpha():
                    current_state = 'letters'
                elif char == '_':
                    current_state = 'underscore'
                    seen_underscore = True
                else:
                    return False

            elif current_state == 'letters':
                if char.isalpha():
                    continue
                elif char == '_':
                    current_state = 'underscore'
                    seen_underscore = True
                else:
                    return False

            elif current_state == 'underscore':
                if char.isupper() and i == len(password) - 1:
                    current_state = 'final_cap'
                elif char.isalpha():
                    continue
                else:
                    return False

            elif current_state == 'final_cap':
                # No characters allowed after final uppercase
                return False

        return current_state == 'final_cap' and seen_underscore

    def draw(self, filename="digit_start_dfa"):
        dot = Digraph(comment="Digit-Start Password DFA")
        dot.attr(rankdir='LR')

        dot.node('', shape='none')
        dot.edge('', 'start')

        for state in self.states:
            shape = 'doublecircle' if state in self.final_states else 'circle'
            dot.node(state, shape=shape)

        dot.edge('start', 'digit', label='0-9')
        dot.edge('digit', 'letters', label='A-Z, a-z')
        dot.edge('digit', 'underscore', label='_')
        dot.edge('letters', 'letters', label='A-Z, a-z')
        dot.edge('letters', 'underscore', label='_')
        dot.edge('underscore', 'underscore', label='A-Z, a-z')
        dot.edge('underscore', 'final_cap', label='A-Z (last char)')

        dot.render(filename, view=True, format='png')
        print(f"DFA graph generated and saved as {filename}.png")


# Example usage
dfa = DigitStartPasswordDFA()

# Get password input from user
user_password = input("Enter a password to check: ")
result = dfa.accepts(user_password)
print(f"Your password is {'ACCEPTED ✅' if result else 'REJECTED ❌'}")

# Draw DFA
dfa.draw("digit_start_dfa")