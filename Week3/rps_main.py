from rps_helper import *

def main():

    option = input('Welcome to Rock, Paper, Scissors!\nOne or two players?: ')
    game_over = False
    player1 = Player(input('Player One, select your name: '))

    if option == '1':
        player2 = Player('Computer')
    else:
        player2 = Player(input('Player Two, select your name: '))
    

    while game_over == False:
        player1.choice = make_selection(player1)
        player2.choice = make_selection(player2) if option == '2' else randomize_choice()

        determine_round(player1, player2)

        display_points(player1, player2)

main()