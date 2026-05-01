# 🎯 QuizMaster Pro

A feature-rich terminal-based **Quiz Application** built with pure Python.  
Designed for learning, fun, and showcasing Python programming skills.

---

## 📌 Features

- 🗂 **3 Quiz Categories** — Python, General CS, General Knowledge
- 🔀 **Randomized Questions** — Different order every time
- 📊 **Score Tracking** — Scores saved persistently to JSON
- 🏆 **Leaderboard** — Top 10 players ranked by performance
- 📈 **Personal History** — Review your past attempts
- ⏱ **Timer per Question** — Tracks how fast you answer
- 🎨 **Colorful Terminal UI** — ANSI-styled, clean interface
- 💡 **Answer Explanations** — Learn why each answer is correct

---

## 🗂 Project Structure

```
quiz_app/
│
├── quiz.py        # Main application file
├── scores.json    # Auto-generated score history (created on first run)
└── README.md      # Project documentation
```

---

## 🚀 How to Run

**Requirements:** Python 3.6+  
No external libraries needed — uses only Python standard library!

```bash
# Clone or download the project
cd quiz_app

# Run the app
python quiz.py
```

---

## 🎮 How to Play

1. Enter your name
2. Choose **Start Quiz** from the main menu
3. Select a category
4. Answer each question (A / B / C / D)
5. See your result, grade, and explanation after each answer
6. View the leaderboard or your history anytime

---

## 📊 Grading System

| Score % | Grade |
|---------|-------|
| 100%    | 🏆 Perfect! |
| 80–99%  | 🌟 Excellent! |
| 60–79%  | 👍 Good Job! |
| 40–59%  | 📚 Keep Practicing |
| 0–39%   | 💪 Try Again! |

---

## 🛠 Tech Stack

| Tool | Usage |
|------|-------|
| Python 3 | Core language |
| `json` | Score persistence |
| `os` | Cross-platform terminal clear |
| `time` | Timer functionality |
| `random` | Question shuffling |
| `datetime` | Timestamp for scores |
| ANSI Escape Codes | Terminal color styling |

---

## 💡 Key Concepts Demonstrated

- File I/O with JSON
- Functions and modular code structure
- Data structures (lists, dictionaries)
- String formatting and ANSI terminal styling
- Sorting and filtering data
- Exception-safe input handling
- Object-like class used for constants

---

## 🔮 Possible Future Enhancements

- [ ] Add difficulty levels (Easy / Medium / Hard)
- [ ] GUI version using `tkinter`
- [ ] Import questions from CSV/JSON file
- [ ] Multiplayer mode
- [ ] Add a countdown timer per question

---

## 👤 Author

**[Your Name]**  
BCA Final Year | Python Developer  
📧 your.email@example.com  
🔗 [LinkedIn](https://linkedin.com) | [GitHub](https://github.com)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
