from turtle import update
import hangman_helper

def update_word_pattern(word, pattern, letter):
        guess_arr = list(pattern)
        for i in range(len(word)):
            if letter == word[i]:
                guess_arr[i] = letter

        return "".join(guess_arr)

print(update_word_pattern('apple','_____', 'a'))