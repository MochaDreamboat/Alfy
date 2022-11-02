secret_word = "giraffe"
guess = ""
tries = 0
guess_limit = 3
out_of_guesses = False
print("Show me what you got")

while guess != secret_word and not (out_of_guesses):
    if tries < guess_limit:
        guess = input("Guess the number: ")
        tries += 1
    else:
        out_of_guesses = True

if guess_limit:
    print("Out of guesses! You lose.")
else:
    print("You win!")