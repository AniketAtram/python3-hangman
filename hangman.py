# importing the random module for making random selection
import random
# importing the list of words which will be used in the game
import hangman_words
# the gui elements of the game
import hangman_art

# a list of all words
words = hangman_words.word_list

# Computer makes a random guess
chosen_word = random.choice(words).lower()

# the boolean value representing if the game is over or not
# this will be used for running while loop
end_of_game = False
# number of acceptable lives.
# There are seven lives corresponding to seven stages of hangman
lives = 7
# print the hangman ASCII art on the screen
print(hangman_art.logo)
# display the blank space represented by dash so that the user
# would know how many letters are present in the word
display = []
for _ in range(len(chosen_word)):
    display += "_"

print(f"{' '.join(display)}")
# running the while loop to run the program until the game is over
while not end_of_game:
    # user makes a guess
    guess = input("Enter a word: ").lower()
    # if the user makes a guess and the letter is already shown
    if guess in display:
        print(f"You've already guessed {guess}")
    # Loop through the various index position in the word
    # and make a linear comparison. If the guess matches a
    # letter in the word, display it in it's appropriate position
    for position in range(len(display)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    # if the word is guessed correctly, User wins!
    if "_" not in display:
        print("Congratulations! You Won!")
        end_of_game = True
        break
    # If user makes a wrong selection, lose a life!
    # If all lives are lost, Game Over!
    if guess not in chosen_word:
        # print("Wrong Choice! Try Again")
        lives -= 1
        # print(f"Lives remaining {lives}")
        if lives == 0:
            end_of_game = True
            print("You Lose!")
            print(f"Correct answer was '{chosen_word}'")
    # Print the hanging man for each consequent step
    print(hangman_art.stages[lives])