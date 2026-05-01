"""
QuizMaster Pro - A Terminal Quiz Application
Author: [Your Name]
Description: A feature-rich quiz app with multiple categories, score tracking,
             leaderboard, and persistent history saved to JSON.
"""

import json
import os
import time
import random
from datetime import datetime

# ─────────────────────────────────────────
#  ANSI Color Codes for Terminal Styling
# ─────────────────────────────────────────
class Color:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BG_BLUE = "\033[44m"
    BG_GREEN= "\033[42m"

def c(text, color):
    return f"{color}{text}{Color.RESET}"

# ─────────────────────────────────────────
#  Questions Bank (3 Categories)
# ─────────────────────────────────────────
QUESTIONS = {
    "🐍 Python": [
        {
            "question": "What is the output of: print(type([]))?",
            "options": ["A) <class 'tuple'>", "B) <class 'list'>", "C) <class 'dict'>", "D) <class 'set'>"],
            "answer": "B",
            "explanation": "[] creates an empty list in Python."
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A) function", "B) func", "C) def", "D) define"],
            "answer": "C",
            "explanation": "'def' is used to define functions in Python."
        },
        {
            "question": "What does 'len([1, 2, 3])' return?",
            "options": ["A) 2", "B) 4", "C) 3", "D) 1"],
            "answer": "C",
            "explanation": "len() returns the number of items in a list."
        },
        {
            "question": "Which of these is a valid Python dictionary?",
            "options": ["A) {1, 2, 3}", "B) [1: 'a']", "C) {'key': 'value'}", "D) (1, 2, 3)"],
            "answer": "C",
            "explanation": "Dictionaries use curly braces with key: value pairs."
        },
        {
            "question": "What is the result of 10 // 3 in Python?",
            "options": ["A) 3.33", "B) 3", "C) 4", "D) 1"],
            "answer": "B",
            "explanation": "// is floor division; 10 // 3 = 3 (discards decimal)."
        },
        {
            "question": "Which method adds an element to the end of a list?",
            "options": ["A) add()", "B) insert()", "C) push()", "D) append()"],
            "answer": "D",
            "explanation": "list.append(item) adds an item to the end of a list."
        },
        {
            "question": "What is the output of: bool(0)?",
            "options": ["A) True", "B) None", "C) False", "D) Error"],
            "answer": "C",
            "explanation": "0 is falsy in Python, so bool(0) returns False."
        },
    ],
    "💻 General CS": [
        {
            "question": "What does CPU stand for?",
            "options": ["A) Central Processing Unit", "B) Computer Processing Utility", "C) Core Program Unit", "D) Central Program Utility"],
            "answer": "A",
            "explanation": "CPU = Central Processing Unit, the brain of the computer."
        },
        {
            "question": "Which data structure works on LIFO principle?",
            "options": ["A) Queue", "B) Array", "C) Stack", "D) Linked List"],
            "answer": "C",
            "explanation": "Stack uses Last In First Out (LIFO) — like a stack of plates."
        },
        {
            "question": "What is the binary representation of decimal 10?",
            "options": ["A) 1010", "B) 1100", "C) 1001", "D) 0110"],
            "answer": "A",
            "explanation": "10 in binary = 8+2 = 1010."
        },
        {
            "question": "What does OOP stand for?",
            "options": ["A) Object Oriented Programming", "B) Online Open Programming", "C) Ordered Object Processing", "D) None of above"],
            "answer": "A",
            "explanation": "OOP = Object Oriented Programming — a programming paradigm."
        },
        {
            "question": "Which sorting algorithm has average O(n log n) complexity?",
            "options": ["A) Bubble Sort", "B) Selection Sort", "C) Merge Sort", "D) Insertion Sort"],
            "answer": "C",
            "explanation": "Merge Sort has O(n log n) average and worst-case complexity."
        },
        {
            "question": "What is RAM?",
            "options": ["A) Read And Modify", "B) Random Access Memory", "C) Rapid Array Module", "D) Remote Access Module"],
            "answer": "B",
            "explanation": "RAM = Random Access Memory, temporary fast storage."
        },
        {
            "question": "What does SQL stand for?",
            "options": ["A) Structured Query Language", "B) Simple Query Logic", "C) Server Query Library", "D) Sequential Query Language"],
            "answer": "A",
            "explanation": "SQL = Structured Query Language for databases."
        },
    ],
    "🌍 General Knowledge": [
        {
            "question": "What is the capital of India?",
            "options": ["A) Mumbai", "B) Kolkata", "C) New Delhi", "D) Chennai"],
            "answer": "C",
            "explanation": "New Delhi is the capital of India."
        },
        {
            "question": "How many planets are in our Solar System?",
            "options": ["A) 7", "B) 8", "C) 9", "D) 10"],
            "answer": "B",
            "explanation": "There are 8 planets after Pluto was reclassified in 2006."
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
            "answer": "D",
            "explanation": "The Pacific Ocean is the largest, covering over 165 million km²."
        },
        {
            "question": "Who invented the telephone?",
            "options": ["A) Thomas Edison", "B) Nikola Tesla", "C) Alexander Graham Bell", "D) Albert Einstein"],
            "answer": "C",
            "explanation": "Alexander Graham Bell is credited with inventing the telephone in 1876."
        },
        {
            "question": "What is the chemical symbol for Gold?",
            "options": ["A) Go", "B) Gd", "C) Gl", "D) Au"],
            "answer": "D",
            "explanation": "Au comes from the Latin word 'Aurum' meaning gold."
        },
        {
            "question": "How many continents are there on Earth?",
            "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "answer": "C",
            "explanation": "There are 7 continents: Asia, Africa, North America, South America, Antarctica, Europe, Australia."
        },
        {
            "question": "What is the speed of light (approx)?",
            "options": ["A) 300,000 km/s", "B) 150,000 km/s", "C) 500,000 km/s", "D) 1,000,000 km/s"],
            "answer": "A",
            "explanation": "Light travels at approximately 299,792 km/s (~300,000 km/s)."
        },
    ]
}

SCORE_FILE = "scores.json"


# ─────────────────────────────────────────
#  Score Management (Persistent JSON)
# ─────────────────────────────────────────
def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            return json.load(f)
    return []

def save_score(name, category, score, total, time_taken):
    scores = load_scores()
    record = {
        "name": name,
        "category": category,
        "score": score,
        "total": total,
        "percentage": round((score / total) * 100, 1),
        "time_taken": round(time_taken, 1),
        "date": datetime.now().strftime("%d %b %Y, %I:%M %p")
    }
    scores.append(record)
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f, indent=2)
    return record


# ─────────────────────────────────────────
#  UI Helpers
# ─────────────────────────────────────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    clear()
    print(c("=" * 55, Color.CYAN))
    print(c("   ██████╗ ██╗   ██╗██╗███████╗", Color.YELLOW))
    print(c("  ██╔═══██╗██║   ██║██║╚══███╔╝", Color.YELLOW))
    print(c("  ██║   ██║██║   ██║██║  ███╔╝ ", Color.YELLOW))
    print(c("  ██║▄▄ ██║██║   ██║██║ ███╔╝  ", Color.YELLOW))
    print(c("  ╚██████╔╝╚██████╔╝██║███████╗", Color.YELLOW))
    print(c("   ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝", Color.YELLOW))
    print(c("     MASTER  PRO  ─  Quiz App", Color.CYAN + Color.BOLD))
    print(c("=" * 55, Color.CYAN))

def print_separator():
    print(c("─" * 55, Color.BLUE))

def get_grade(percentage):
    if percentage == 100:
        return "🏆 PERFECT!", Color.GREEN
    elif percentage >= 80:
        return "🌟 Excellent!", Color.GREEN
    elif percentage >= 60:
        return "👍 Good Job!", Color.YELLOW
    elif percentage >= 40:
        return "📚 Keep Practicing", Color.MAGENTA
    else:
        return "💪 Try Again!", Color.RED


# ─────────────────────────────────────────
#  Core Quiz Logic
# ─────────────────────────────────────────
def run_quiz(name, category):
    questions = QUESTIONS[category].copy()
    random.shuffle(questions)

    score = 0
    total = len(questions)
    start_time = time.time()
    results = []

    for i, q in enumerate(questions, 1):
        clear()
        print_banner()
        print(c(f"\n  Player : {name}", Color.WHITE))
        print(c(f"  Category: {category}", Color.CYAN))
        print(c(f"  Score  : {score}/{i-1}", Color.GREEN))
        print_separator()

        # Progress bar
        progress = int((i - 1) / total * 30)
        bar = "█" * progress + "░" * (30 - progress)
        print(f"\n  [{c(bar, Color.CYAN)}] Q{i}/{total}\n")

        print(c(f"  {q['question']}", Color.WHITE + Color.BOLD))
        print()
        for opt in q["options"]:
            print(f"    {c(opt, Color.CYAN)}")
        print()

        # Get answer with timer
        q_start = time.time()
        while True:
            ans = input(c("  ➤ Your answer (A/B/C/D): ", Color.YELLOW)).strip().upper()
            if ans in ["A", "B", "C", "D"]:
                break
            print(c("  ⚠ Please enter A, B, C, or D only.", Color.RED))

        q_time = round(time.time() - q_start, 1)
        correct = ans == q["answer"]

        if correct:
            score += 1
            print(c("\n  ✅ CORRECT!", Color.GREEN + Color.BOLD))
        else:
            print(c(f"\n  ❌ Wrong! Correct answer: {q['answer']}", Color.RED + Color.BOLD))

        print(c(f"  💡 {q['explanation']}", Color.MAGENTA))
        print(c(f"  ⏱ Time taken: {q_time}s", Color.BLUE))
        results.append({"question": q["question"], "correct": correct, "your_ans": ans, "correct_ans": q["answer"]})

        input(c("\n  Press ENTER for next question...", Color.WHITE))

    total_time = time.time() - start_time
    record = save_score(name, category, score, total, total_time)
    show_result(name, score, total, total_time, results, record)


# ─────────────────────────────────────────
#  Result Screen
# ─────────────────────────────────────────
def show_result(name, score, total, total_time, results, record):
    clear()
    print_banner()
    pct = record["percentage"]
    grade, grade_color = get_grade(pct)

    print(c(f"\n  🎉 Quiz Complete! — {name}", Color.CYAN + Color.BOLD))
    print_separator()
    print(c(f"\n  Score      : {score} / {total}", Color.WHITE))
    print(c(f"  Percentage : {pct}%", Color.YELLOW))
    print(c(f"  Grade      : {grade}", grade_color + Color.BOLD))
    print(c(f"  Time Taken : {record['time_taken']}s", Color.BLUE))
    print(c(f"  Date       : {record['date']}", Color.WHITE))
    print_separator()

    # Summary table
    print(c("\n  📋 Answer Summary:\n", Color.CYAN))
    for i, r in enumerate(results, 1):
        status = c("✅", Color.GREEN) if r["correct"] else c("❌", Color.RED)
        short_q = r["question"][:45] + "..." if len(r["question"]) > 45 else r["question"]
        print(f"  {status} Q{i}: {short_q}")
        if not r["correct"]:
            print(c(f"       You: {r['your_ans']}  |  Correct: {r['correct_ans']}", Color.RED))

    print()


# ─────────────────────────────────────────
#  Leaderboard
# ─────────────────────────────────────────
def show_leaderboard():
    clear()
    print_banner()
    print(c("\n  🏆 LEADERBOARD — Top 10 Scores\n", Color.YELLOW + Color.BOLD))
    print_separator()

    scores = load_scores()
    if not scores:
        print(c("\n  No scores yet. Play a quiz to get on the board!\n", Color.MAGENTA))
        input(c("  Press ENTER to go back...", Color.WHITE))
        return

    # Sort by percentage, then by time
    sorted_scores = sorted(scores, key=lambda x: (-x["percentage"], x["time_taken"]))[:10]

    medals = ["🥇", "🥈", "🥉"] + ["🔹"] * 7
    print(f"  {'#':<4} {'Name':<14} {'Category':<22} {'Score':<8} {'%':<7} {'Time'}")
    print(c("  " + "─" * 65, Color.BLUE))

    for i, s in enumerate(sorted_scores):
        cat_short = s["category"].split()[-1]  # just the text part
        line = f"  {medals[i]} {s['name']:<14} {cat_short:<22} {s['score']}/{s['total']:<5}  {s['percentage']}%  {s['time_taken']}s"
        color = Color.YELLOW if i == 0 else Color.WHITE
        print(c(line, color))

    print()
    input(c("  Press ENTER to go back...", Color.WHITE))


# ─────────────────────────────────────────
#  Score History
# ─────────────────────────────────────────
def show_history(name):
    clear()
    print_banner()
    print(c(f"\n  📈 Score History — {name}\n", Color.CYAN + Color.BOLD))
    print_separator()

    scores = load_scores()
    my_scores = [s for s in scores if s["name"].lower() == name.lower()]

    if not my_scores:
        print(c("\n  No history found for your name.\n", Color.MAGENTA))
    else:
        for i, s in enumerate(reversed(my_scores[-10:]), 1):
            grade, col = get_grade(s["percentage"])
            print(c(f"  {i}. [{s['date']}]", Color.BLUE))
            print(f"     Category : {s['category']}")
            print(f"     Score    : {s['score']}/{s['total']}  ({s['percentage']}%)  {c(grade, col)}")
            print(f"     Time     : {s['time_taken']}s\n")

    input(c("  Press ENTER to go back...", Color.WHITE))


# ─────────────────────────────────────────
#  Main Menu
# ─────────────────────────────────────────
def main():
    print_banner()
    print(c("\n  Welcome to QuizMaster Pro!\n", Color.CYAN))
    name = input(c("  Enter your name: ", Color.YELLOW)).strip()
    if not name:
        name = "Player"

    while True:
        clear()
        print_banner()
        print(c(f"\n  Hello, {name}! 👋\n", Color.GREEN))
        print(c("  ┌─────────────────────────────┐", Color.CYAN))
        print(c("  │        MAIN MENU            │", Color.CYAN))
        print(c("  ├─────────────────────────────┤", Color.CYAN))
        print(c("  │  1. Start Quiz              │", Color.WHITE))
        print(c("  │  2. View Leaderboard        │", Color.WHITE))
        print(c("  │  3. My Score History        │", Color.WHITE))
        print(c("  │  4. Change Player           │", Color.WHITE))
        print(c("  │  5. Exit                    │", Color.WHITE))
        print(c("  └─────────────────────────────┘", Color.CYAN))

        choice = input(c("\n  ➤ Choose (1-5): ", Color.YELLOW)).strip()

        if choice == "1":
            # Category selection
            clear()
            print_banner()
            print(c("\n  📚 Choose a Category:\n", Color.CYAN))
            categories = list(QUESTIONS.keys())
            for i, cat in enumerate(categories, 1):
                print(c(f"  {i}. {cat} ({len(QUESTIONS[cat])} questions)", Color.WHITE))

            cat_choice = input(c("\n  ➤ Enter category number: ", Color.YELLOW)).strip()
            if cat_choice in ["1", "2", "3"]:
                run_quiz(name, categories[int(cat_choice) - 1])
            else:
                print(c("\n  Invalid choice.", Color.RED))
                time.sleep(1)

        elif choice == "2":
            show_leaderboard()

        elif choice == "3":
            show_history(name)

        elif choice == "4":
            name = input(c("  Enter new name: ", Color.YELLOW)).strip() or name

        elif choice == "5":
            clear()
            print_banner()
            print(c("\n  Thanks for playing QuizMaster Pro! 🎓\n", Color.GREEN + Color.BOLD))
            print(c("  Keep learning, keep growing! 🚀\n", Color.CYAN))
            break
        else:
            print(c("  Invalid choice. Try again.", Color.RED))
            time.sleep(1)


if __name__ == "__main__":
    main()
