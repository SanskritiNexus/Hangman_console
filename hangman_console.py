import random
import requests

# Function to fetch random word from API
def get_random_word():
    url = "https://random-word-api.herokuapp.com/word"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()[0].upper()
    except:
        pass
    # Agar API fail ho jaye to fallback words
    return random.choice(["PYTHON", "DEVELOPER", "HANGMAN", "PROGRAMMING"]).upper()

def hangman():
    word = get_random_word()
    guessed = ["_"] * len(word)
    guessed_letters = set()
    lives = 6

    print("🎮 Welcome to Hangman!")
    print("Guess the word:", " ".join(guessed))

    while lives > 0 and "_" in guessed:
        guess = input("👉 Enter a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print("✅ Correct!", " ".join(guessed))
        else:
            lives -= 1
            print(f"❌ Wrong! Lives left: {lives}")

    if "_" not in guessed:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("💀 Game Over! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()
