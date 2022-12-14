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
    # Guesses must be:
    # One character
    # Lowercase letters only
    # No numbers
    if char.isalpha() == True and char.islower() == True:
        return True
    return False

def validate_word(word):
    for char in word:
        if validate_entry(char) == False:
            return False
        return True

def validate_pattern(word, pattern):
    for i in range(len(word)):
        if word[i] != pattern[i] and pattern[i] != '_':
            return False
    return True
            
def verify_chars(word, wrong_letters):
    for char in wrong_letters:
        if word.count(char) != 0:
            return False
    return True

def filter_words_list(words, pattern, wrong_guess_list):
    # Creates shallow copy of words list for filtering
    possible_solutions = []
    wrong_letters = [guess for guess in wrong_guess_list if len(guess) == 1]

    for word in words:
        # Append possible_solutions if length matches
        if len(word) == len(pattern):
            possible_solutions.append(word)
            print(len(possible_solutions))
    
    possible_solutions = [word for word in possible_solutions if validate_pattern(word, pattern) and verify_chars(word, wrong_letters)]

    return possible_solutions


def run_single_game(list_words, score=POINTS_INITIAL):
    word_to_guess = get_random_word(list_words)
    pattern = "_" * len(word_to_guess)
    wrong_guess_lst = []
    game_over = False

    print(word_to_guess)

    message = "Guess a letter/word...or ask for a hint!"

    while game_over == False:
        display_state(pattern, wrong_guess_lst, score, message)
        choice = get_input()
        entry = choice[1]

        # Directions if user is guessing an individual letter
        if choice[0] == LETTER:
            if validate_entry(entry) == False or len(entry) > 1:
                message = "Invalid input! Try again"
                continue
            if entry in pattern or entry in wrong_guess_lst:
                message = "Already guessed that! Try again"
                continue
            
            score -= 1
            if entry not in word_to_guess:
                wrong_guess_lst.append(entry)
                message = "Letter not in word. Try again."
            
            appearances = word_to_guess.count(entry)
            pattern = update_word_pattern(word_to_guess, pattern, entry)
            score += (appearances * (appearances+1) // 2)
            message = 'Keep guessing!'

        # Directions if user is guessing a whole word
        if choice[0] == WORD:
            if validate_word(entry) == False:
                message = 'Please enter a valid word.'
                continue

            score -= 1
            unsolved = pattern.count("_")
            if entry == word_to_guess:
                pattern = word_to_guess
                score += (unsolved*(unsolved-1) // 2)
            else:
                wrong_guess_lst.append(entry)
                message = 'That\'s not the word. Try again!'

        if choice[0] == HINT:
            score -= 1
            hint_list = filter_words_list(list_words, pattern, wrong_guess_lst)
            current_length = len(hint_list)

            if current_length > HINT_LENGTH:
                hint_list = [hint_list[(i * current_length) // HINT_LENGTH] for i in range(HINT_LENGTH)]

            show_suggestions(hint_list)

        if pattern == word_to_guess:
            message = 'Congrats! You got the word!'
            game_over = True

        if score == 0:
            message = f'Sorry, bud! The answer was {word_to_guess}'
            game_over = True

    display_state(pattern, wrong_guess_lst, score, message)

    return score


def main():
    games_played = 0
    words = load_words()
    active_game = True
    current_points = POINTS_INITIAL

    while active_game == True:
        current_points = run_single_game(words, current_points)
        
        if current_points > 0:
            games_played += 1
            active_game = play_again(f"""
            You have scored {current_points} so far across {games_played} games.
            Play again?""")

        elif current_points == 0:
            current_points = POINTS_INITIAL
            active_game = play_again(f"You have lasted for {games_played} games. Wanna give it another go?")
            games_played = 0

if __name__ == "__main__":
    main()