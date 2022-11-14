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

def validate_word(word):
    for char in word:
        if validate_entry(char) == False:
            return False
        return True
    
def run_single_game(list_words, score=POINTS_INITIAL):
    word_to_guess = get_random_word(list_words)
    pattern = "_" * len(word_to_guess)
    wrong_guess_lst = []

    print(word_to_guess)

    game_over = False
    message = "Guess a letter/word...or ask for a hint!"

    while game_over == False or score != 0:
        display_state(pattern, wrong_guess_lst, score, message)
        choice = get_input()
        entry = choice[1]

        if choice[0] == LETTER:
            if validate_entry(entry) == False or len(entry) > 1:
                message = "Invalid input! Try again"
                continue
            elif entry in pattern or entry in wrong_guess_lst:
                message = "Already guessed that! Try again"
                continue
            
            score -= 1
            if entry not in word_to_guess:
                wrong_guess_lst.append(entry)
                message = "Letter not in word. Try again."
                continue
            
            appearances = word_to_guess.count(entry)
            pattern = update_word_pattern(word_to_guess, pattern, entry)
            score += (appearances * (appearances+1) // 2)
            continue

        if choice[0] == WORD:
            if validate_word == False:
                message = 'Please enter a valid word.'
                continue

            score -= 1
            unsolved = pattern.count("_")
            if entry == word_to_guess:
                pattern = word_to_guess
                game_over = True
                score += (unsolved*(unsolved-1) // 2)


words = load_words()
run_single_game(words)