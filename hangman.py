import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def play(word):
    word_completion = "_" * len(word)
    guess = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guess and tries > 0:
        Guess = input("Please enter a letter or word: ").upper()
        if len(Guess) == 1 and guess.isalpha():
            if Guess in guessed_letters:
                print("You already guessed the letter", Guess)
            elif Guess not in word:
                print(Guess,"is not in the word.")
                tries -= 1
                guessed_letters.append(Guess)
            else:
                print("Good job,", Guess, "is in the word!")
                guessed_letters.append(Guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == Guess]
                for index in indices:
                    word_as_list[index] = Guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guess = True


        elif len(Guess) == len(word) and Guess.isalpha():
            if Guess in guessed_words:
                print("You already guessed the word", Guess)
            elif Guess != word:
                print(Guess, "is not the word.")
                tries -= 1
                guessed_words.append(Guess)
            else:
                guess = True
                word_completion = word

        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guess:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word +". Maybe next time!")



def main():
    word = get_word()
    play(word)
    while input("Play Again ? (Y/N) ").upper() == 'Y':
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
