# Task 01 By Avi Bhosale for the company       


import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def print_welcome():
    print(Fore.CYAN + Style.BRIGHT + "🎉 Welcome to Hangman - Internship Edition! 🎉 By Avishkar Bhosale")
    print(Fore.YELLOW + "Guess the word, one letter at a time.")
    print("You have 6 incorrect guesses. Let's begin!\n")

def get_random_word():
    word_list = ['python', 'logic', 'intern', 'script', 'debug']
    return random.choice(word_list).lower()

def display_current_progress(secret_word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])

def hangman_game():
    print_welcome()
    secret_word = get_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    while incorrect_guesses < max_attempts:
        current_display = display_current_progress(secret_word, guessed_letters)
        print(Fore.BLUE + f"\nWord: {current_display}")
        print(Fore.MAGENTA + f"Guessed letters: {' '.join(guessed_letters)}")
        print(Fore.YELLOW + f"Incorrect attempts left: {max_attempts - incorrect_guesses}")

        guess = input(Fore.WHITE + "Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print(Fore.YELLOW + "⚠️  Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print(Fore.YELLOW + "🔁 You've already guessed that letter. Try again.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(Fore.GREEN + "✅ Good guess!\n")
        else:
            incorrect_guesses += 1
            print(Fore.RED + "❌ Incorrect guess!\n")

        if all(letter in guessed_letters for letter in secret_word):
            print(Fore.CYAN + Style.BRIGHT + f"\n🎊 Congratulations! You guessed the word: {secret_word.upper()}")
            break
    else:
        print(Fore.RED + Style.BRIGHT + f"\n💀 Game Over! The word was: {secret_word.upper()}")

if __name__ == "__main__":
    hangman_game()
