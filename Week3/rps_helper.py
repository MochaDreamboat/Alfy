import random

win_conditions = {
    'rs': 1,
    'sp': 1,
    'pr': 1,
}

POINTS_TO_WIN = 3

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.wins = 0
        self.choice = ''

    def add_point(player):
        player.points += 1

    def add_wins(player):
        player.wins += 1

    def reset_points(player):
        player.points = 0

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
        print('Tie!')
        return None

    winner = player1 if f'{player1.choice}{player2.choice}' in win_conditions.keys() else player2

    winner.add_point()
    print(f'{winner.name} wins this one!')

def display_points(p1, p2):
    print(f'{p1.name} - {p1.points} / {p2.name} - {p2.points}')

def check_win(player1, player2):
    for player in [player1, player2]:
        if player.points == POINTS_TO_WIN:

            print(f'{player.name} wins!')
            return True
    return False