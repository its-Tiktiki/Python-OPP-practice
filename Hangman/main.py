import random
from hangman_art import logo, CHEERING_GIRL, HANGMAN_DRAWINGS, BYE_GIRL

print(logo)

def keep_playing():
    while True:
        play_again = input("Do you wanna play a round of hangman? yes/no: ")
        if play_again.lower() == "yes":
            return True
        elif play_again.lower() == "no":
            print(BYE_GIRL[0])
            return False
        else:
            print("wrong input. Please try again.")


def get_word_to_guess():
    all_words = ["chocolate", "purple", "bangtan", "seventeen", "army", "jungkoon", "taehyung", "jimin", "jhope", "suga", "jin", "namjoon"]
    word_to_guess = random.choice(all_words)
    return word_to_guess

# takes word parameter to return its dashed form
def get_dashed_word(word):
    word_dashed = ""
    for i in range(len(word)):
        word_dashed += "_"
    return word_dashed


# calls the keep_playing function to get boolean value and starts running if the value is true
while keep_playing():
    main_word = get_word_to_guess()
    dashed_word = get_dashed_word(main_word)
    print(f"Word to Guess : {dashed_word}")
    MAX_ATTEMPTS = 0
    guessed_letters = ""
    game_on = True

    # it keeps running while the round is not over
    while game_on:
        display = ""
        user_guess = input("Guess a letter: ")
        if user_guess in main_word and user_guess not in guessed_letters:
            guessed_letters+=user_guess
            for letter in main_word:
                if letter in guessed_letters:
                    display += letter
                else:
                    display += "_"
            if main_word == display:
                game_on = False
                print("Game Over. You Won!")
                print(CHEERING_GIRL[0])
            print(display)
        else:
            if MAX_ATTEMPTS == 5:
                game_on = False
                print("Game Over. You Lose...")
            else:
                print(HANGMAN_DRAWINGS[MAX_ATTEMPTS])
                MAX_ATTEMPTS += 1
