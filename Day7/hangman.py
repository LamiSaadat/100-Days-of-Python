import random
import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for i, letter in enumerate(chosen_word):
        if guess == letter:
            display[i] = guess
    
    if guess not in chosen_word:
        print(f"{guess} is not in the word")
        lives-=1
        if lives == 0:
            end_of_game = True
            print("You lose :(")
    
    print(f"{' '.join(display)}")
 
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(hangman_art.stages[lives])