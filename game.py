import random

def get_random_word():
    words = ["python", "developer", "github", "programming", "gaming"]
    return random.choice(words)

def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        # Display current word status
        display = [letter if letter in guessed_letters else "_" for letter in word]
        print("\nWord:", " ".join(display))
        
        if "_" not in display:
            print("You won!")
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Wrong! Attempts remaining: {attempts}")

    print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()
