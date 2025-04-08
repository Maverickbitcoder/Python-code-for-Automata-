from graphviz import Digraph

class GmailFA:
    def __init__(self):
        self.states = {
            'S0': 'initial',
            'S1': None,  # Username
            'S2': None,  # After @
            'S3': None,  # g
            'S4': None,  # m
            'S5': None,  # a
            'S6': None,  # i
            'S7': None,  # l
            'S8': None,  # .
            'S9': None,  # c
            'S10': None,  # o
            'S11': 'accept'  # m
        }
        self.current_state = 'S0'
        self.transition_log = []

    def reset(self):
        self.current_state = 'S0'
        self.transition_log = []

    def is_username_char(self, c):
        return c.isalnum() or c in ['.', '_', '%', '+', '-']

    def process_input(self, email):
        self.reset()
        email = email.lower()  # Gmail addresses are case-insensitive
        for idx, char in enumerate(email):
            from_state = self.current_state
            to_state = None

            if from_state == 'S0':
                if self.is_username_char(char):
                    to_state = 'S1'
                else:
                    return False, f"Invalid username character '{char}' at position {idx}"

            elif from_state == 'S1':
                if char == '@':
                    to_state = 'S2'
                elif self.is_username_char(char):
                    to_state = 'S1'
                else:
                    return False, f"Invalid username character '{char}' at position {idx}"

            # Validate 'gmail.com' sequence
            elif from_state == 'S2':
                to_state = 'S3' if char == 'g' else None
            elif from_state == 'S3':
                to_state = 'S4' if char == 'm' else None
            elif from_state == 'S4':
                to_state = 'S5' if char == 'a' else None
            elif from_state == 'S5':
                to_state = 'S6' if char == 'i' else None
            elif from_state == 'S6':
                to_state = 'S7' if char == 'l' else None
            elif from_state == 'S7':
                to_state = 'S8' if char == '.' else None
            elif from_state == 'S8':
                to_state = 'S9' if char == 'c' else None
            elif from_state == 'S9':
                to_state = 'S10' if char == 'o' else None
            elif from_state == 'S10':
                to_state = 'S11' if char == 'm' else None
            elif from_state == 'S11':
                return False, f"Extra character '{char}' after valid address"

            if to_state is None:
                expected = self.get_expected_char(from_state)
                return False, f"Expected {expected} at position {idx}, got '{char}'"

            self.transition_log.append((from_state, char, to_state))
            self.current_state = to_state

        if self.current_state == 'S11':
            return True, "Valid Gmail address"
        else:
            return False, f"Incomplete address - ended in state {self.current_state}"

    def get_expected_char(self, state):
        expectations = {
            'S2': "'g' after @",
            'S3': "'m' after g",
            'S4': "'a' after m",
            'S5': "'i' after a",
            'S6': "'l' after i",
            'S7': "'.' after l",
            'S8': "'c' after .",
            'S9': "'o' after c",
            'S10': "'m' after o",
            'S11': "end of address"
        }
        return expectations.get(state, "valid username character")

    def visualize(self):
        dot = Digraph(comment='Gmail FA')

        # Add states
        for state, attr in self.states.items():
            if attr == 'initial':
                dot.node(state, shape='point')
            elif attr == 'accept':
                dot.node(state, shape='doublecircle')
            else:
                dot.node(state, shape='circle')

        # Add transitions
        dot.edge('S0', 'S1', label='a-z, 0-9, ._%+-')
        dot.edge('S1', 'S1', label='a-z, 0-9, ._%+-')
        dot.edge('S1', 'S2', label='@')
        dot.edge('S2', 'S3', label='g')
        dot.edge('S3', 'S4', label='m')
        dot.edge('S4', 'S5', label='a')
        dot.edge('S5', 'S6', label='i')
        dot.edge('S6', 'S7', label='l')
        dot.edge('S7', 'S8', label='.')
        dot.edge('S8', 'S9', label='c')
        dot.edge('S9', 'S10', label='o')
        dot.edge('S10', 'S11', label='m')

        return dot


# Get user input
email = input("Enter email address to validate: ").strip()

# Validate using FA
validator = GmailFA()
is_valid, message = validator.process_input(email)

# Show results
print("\nValidation Result:")
print(f"Email: {email}")
print(f"Status: {message}")
print("\nTransition Path:")
for transition in validator.transition_log:
    print(f"{transition[0]} --'{transition[1]}'--> {transition[2]}")

# Generate visualization
dot = validator.visualize()
dot.render('gmail_fa', view=True, format='png')
print("\nFinite Automaton diagram saved as 'gmail_fa.png'")