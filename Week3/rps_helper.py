import random

win_conditions = {
    'rs': 1,
    'sp': 1,
    'pr': 1,
}

class Player:
    points = 0
    choice = 0

    def __init__(self, name):
        self.name = name

    def add_point():
        points += 1

def make_selection(player):
    choice = input(f'{player.name}, Rock, paper, or scissors?')

    if validate_choice(choice) == False:
        print('Please pick a valid selection. Rock (r), paper (p) or scissors (s)!')
        return make_selection(player)

    return choice

# Used during AI games. Randomly picks among r, p, or s.
def randomize_choice():
    choices = 'rps'
    return choices[random.randint(0, 2)]

# Returns false (as a means of restarting step) if user enters invalid character
def validate_choice(selection):
    choices = 'RrPpSs'

    if selection not in choices:
        return False
    
    return True

# Should take in player functions as callbacks.
# Match with appropriate condition object.
def determine_round(player1, player2):
    if player1.choice == player2.choice:
        return None

    winner = player1 if f'{player1.choice}{player2.choice}' in win_conditions else player2

    winner.add_point()
    print(f'{winner.name} wins this one!')

def display_points(p1, p2):
    return f'{p1.name} - {p1.points} / {p2.name} - {p2.points}'

def check_win(score, score_to_win):
    if score == score_to_win:
        return True
    return False