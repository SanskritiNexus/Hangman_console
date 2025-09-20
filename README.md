# 🎮 Hangman Console Game

A simple Python console-based **Hangman** game where you guess letters to reveal a hidden word.  
The game fetches random words from an online API and falls back to predefined words if the API is unavailable.

---

## ✨ Features
- Fetches random words using [Random Word API](https://random-word-api.herokuapp.com/).
- Fallback word list in case of API failure.
- Tracks lives (default: 6).
- Prevents repeated guesses.
- Console-based gameplay with clear instructions.

---

## 📂 Project Structure
```
hangman_console.py   # Main game script
```

---

## 🚀 How to Run

1. Clone or download this repository.
2. Install required dependencies:
   ```bash
   pip install requests
   ```
3. Run the game:
   ```bash
   python hangman_console.py
   ```

---

## 🕹️ Gameplay
- The game shows blanks (`_`) for each letter of the hidden word.  
- Enter one letter at a time to guess the word.  
- You lose a life for each incorrect guess.  
- The game ends when:
  - You correctly guess the full word 🎉  
  - OR you run out of lives 💀  

---

## 📦 Dependencies
- Python 3.7+
- `requests` library

---

## 🔮 Future Enhancements
- Add ASCII art for hangman stages.
- Support multiplayer mode.
- Add difficulty levels.
- Word categories (Animals, Countries, etc.).

---

## 📝 License
This project is licensed under the MIT License — feel free to use and modify.
