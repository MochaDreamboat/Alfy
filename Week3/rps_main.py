from rps_helper import *

def main():

    option = input('Welcome to Rock, Paper, Scissors!\n One or two players?: ')
    game_over = False
    player1 = Player(input('Player One, select your name: '))

    if option == 1:
        player2 = Player('Computer')
    else:
        player2 = Player(input('Player Two, select your name: '))
    

    while game_over == False:
        p1_choice = input(f'Player One...rock, paper, or scissors?: ' )

        if validate_choice(p1_choice) == False:
            continue

        if option == 1:
            p2_choice = randomize_choice()
