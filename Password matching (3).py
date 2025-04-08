#1.	Starts with at least one uppercase letter.
#2.	Can have lowercase letters.
#3.	Must have at least one digit.
#4.	Ends with exactly one special character from: !, @, or #.
#5.	No characters allowed after the special character.

from graphviz import Digraph

class PasswordDFA:
    def __init__(self):
        self.states = {'start', 'uppercase', 'lowercase', 'digit', 'special'}
        self.final_states = {'special'}
        self.start_state = 'start'

    def accepts(self, password):
        current_state = self.start_state
        seen_digit = False
        seen_upper = False

        for i, char in enumerate(password):
            if current_state == 'start':
                if char.isupper():
                    current_state = 'uppercase'
                    seen_upper = True
                else:
                    return False

            elif current_state == 'uppercase':
                if char.isupper():
                    continue
                elif char.islower():
                    current_state = 'lowercase'
                elif char.isdigit():
                    current_state = 'digit'
                    seen_digit = True
                else:
                    return False

            elif current_state == 'lowercase':
                if char.islower():
                    continue
                elif char.isdigit():
                    current_state = 'digit'
                    seen_digit = True
                else:
                    return False

            elif current_state == 'digit':
                if char.isdigit():
                    continue
                elif char in "!@#":
                    if seen_digit and i == len(password) - 1:  # Last character
                        current_state = 'special'
                    else:
                        return False
                else:
                    return False

            elif current_state == 'special':
                # No characters allowed after special character
                return False

        return current_state == 'special'

    def draw(self, filename="password_dfa_v2"):
        dot = Digraph(comment="Password DFA with lowercase")
        dot.attr(rankdir='LR')

        # Invisible start arrow
        dot.node('', shape='none')
        dot.edge('', 'start')

        # Add nodes
        for state in self.states:
            shape = 'doublecircle' if state in self.final_states else 'circle'
            dot.node(state, shape=shape)

        # Add transitions
        dot.edge('start', 'uppercase', label='A-Z')
        dot.edge('uppercase', 'uppercase', label='A-Z')
        dot.edge('uppercase', 'lowercase', label='a-z')
        dot.edge('lowercase', 'lowercase', label='a-z')
        dot.edge('uppercase', 'digit', label='0-9')
        dot.edge('lowercase', 'digit', label='0-9')
        dot.edge('digit', 'digit', label='0-9')
        dot.edge('digit', 'special', label='!, @, #')

        # Render the DFA
        dot.render(filename, view=True, format='png')
        print(f"DFA graph generated and saved as {filename}.png")


# Instantiate DFA
dfa = PasswordDFA()

# Ask user for input
user_password = input("Enter a password to validate: ")

# Check validity
if dfa.accepts(user_password):
    print("Password ACCEPTED ✅")
else:
    print("Password REJECTED ❌")

# Optional: Draw the DFA graph
dfa.draw("password_dfa_v2")