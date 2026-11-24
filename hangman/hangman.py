import random


def play_game():
    words = ["python", "java", "javascript", "php"]
    secret_word = random.choice(words)
    masked = ["-"] * len(secret_word)
    tried_letters = set()
    attempts = 8

    while attempts > 0:
        print("".join(masked))
        letter = input("Input a letter: > ")

        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if not ("a" <= letter <= "z"):
            print("Please enter a lowercase English letter")
            continue
        if letter in tried_letters:
            print("You've already guessed this letter")
            continue

        tried_letters.add(letter)

        if letter in secret_word:
            for i, ch in enumerate(secret_word):
                if ch == letter:
                    masked[i] = letter
            if "-" not in masked:
                print("".join(masked))
                print(f"You guessed the word {secret_word}!")
                print("You survived!")
                return
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1

    print("You lost!")


def main():
    print("HANGMAN")
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: > ')
        if choice == "play":
            play_game()
        elif choice == "exit":
            break


if __name__ == "__main__":
    main()