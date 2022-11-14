from turtle import update
from wsgiref import validate
from hangman_helper import *

def update_word_pattern(word, pattern, letter):
    # End condition:
    # Pattern is fully revealed and points >0
    
    #No Repeat incorrect guesses
        guess_arr = list(pattern)
        for i in range(len(word)):
            if letter == word[i]:
                guess_arr[i] = letter

        return "".join(guess_arr)

def validate_entry(char):
    # Guesses must be one character
    # lowercase letters only
    # no numbers
    if char.isalpha() == True and char.islower() == True:
        return True
    return False
    
def run_single_game(list_words, score=18):
    word_to_guess = get_random_word(list_words)
    pattern = "_" * len(word_to_guess)
    wrong_guess_lst = []

    game_over = False
    message = "Guess a letter/word...or ask for a hint!"

    while game_over == False:
        display_state(pattern, wrong_guess_lst, score, message)
        choice = get_input()
        entry = choice[1]
    
        if choice[0] == 1:
            if validate_entry(entry) == False or len(entry) > 1:
                message = "Invalid input! Try again"
                continue
            if entry in pattern:
                message = "Already guessed that! Try again"
                continue
            score -= 1
            if entry not in word_to_guess:
                message = "Letter not in word. Try again."
                continue
            
            pattern = update_word_pattern(word_to_guess, pattern, entry)
            score += word_to_guess.count(entry)
            continue

words = load_words()
run_single_game(words)