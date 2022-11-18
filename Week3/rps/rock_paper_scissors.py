from rock_paper_scissors_helper import *

def main():

    option = check_input('Welcome to Rock, Paper, Scissors!\nOne or two players?: ')
    game_over = False
    player1 = Player(check_input('Player One, select your name: '))

    if option == '1':
        player2 = Player('Computer')
    else:
        player2 = Player(check_input('Player Two, select your name: '))
    

    while game_over == False:
        player1.choice = make_selection(player1)
        player2.choice = make_selection(player2) if option == '2' else randomize_choice()

        print(f'{player1.name} chose {player1.choice}, {player2.name} chose {player2.choice}')
        determine_round(player1, player2)
        game_over = check_win(player1, player2)
        display_points(player1, player2)

    # Asks player if they want to play again.
    while True:
        response = check_input('Want to go another round?')
        if  response == 'y':
            print('Let\'s roll!\n\n')
            return main()
        elif response == 'n':
            print('Thanks for playing!')
            exit()
        else:
            print('Make up your mind!')
            continue


if __name__ == "__main__":
    main()