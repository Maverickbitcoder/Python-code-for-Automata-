"""
Password Rules:
	1.	 Starts with at least one uppercase letter (A-Z)
	2.	 Followed by at least one lowercase letter (a-z)
	3.	 Followed by at least one digit (0-9)
	4.	 Must end with a digit — no characters allowed after the digits
"""
from graphviz import Digraph

class PasswordDFA:
    def __init__(self):
        self.states = {'start', 'uppercase', 'lowercase', 'digit'}
        self.final_states = {'digit'}  # Accept only if ends in digit
        self.start_state = 'start'

    def accepts(self, password):
        current_state = self.start_state
        seen_upper = False
        seen_lower = False
        seen_digit = False

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
                    seen_lower = True
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
                else:
                    return False  # Nothing allowed after digits

        # Final check: must have seen all three and end in digit
        return current_state == 'digit' and seen_upper and seen_lower and seen_digit

    def draw_dfa(self, filename="password_dfa_end_digit"):
        dot = Digraph(comment="Password DFA ending with digit")
        dot.attr(rankdir='LR')

        # Start arrow
        dot.node('', shape='none')
        dot.edge('', 'start')

        # States
        for state in self.states:
            shape = 'doublecircle' if state in self.final_states else 'circle'
            dot.node(state, shape=shape)

        # Transitions
        dot.edge('start', 'uppercase', label='A-Z')
        dot.edge('uppercase', 'uppercase', label='A-Z')
        dot.edge('uppercase', 'lowercase', label='a-z')
        dot.edge('lowercase', 'lowercase', label='a-z')
        dot.edge('lowercase', 'digit', label='0-9')
        dot.edge('digit', 'digit', label='0-9')

        # Render
        dot.render(filename, view=True, format='png')
        print(f"DFA saved as '{filename}.png'")


# --- Main Program ---
if __name__ == "__main__":
    dfa = PasswordDFA()
    user_password = input("Enter a password to check: ")

    if dfa.accepts(user_password):
        print("✅ Password ACCEPTED")
    else:
        print("❌ Password REJECTED")

    dfa.draw_dfa("password_dfa_end_digit")