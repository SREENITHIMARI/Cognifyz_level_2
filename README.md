# COGNIFYZ - Task Manager

A comprehensive Python project with multiple interactive tasks and games.

## 📁 Project Structure

```
cognifyz_2/
├── main.py                                    # Main menu system
├── README.md                                  # This file
├── task_1_guessing_game/
│   └── guessing_game.py                      # 1-100 guessing game
├── task_2_custom_guesser/
│   └── custom_guesser.py                     # Custom range number guesser
├── task_3_password_checker/
│   └── password_checker.py                   # Password strength analyzer
├── task_4_fibonacci/
│   └── fibonacci.py                          # Fibonacci sequence generator
└── task_5_word_count/
    └── word_count.py                         # File analysis & word count
```

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Running the Program

1. **Navigate to the project directory:**
   ```bash
   cd c:\Users\sreen\OneDrive\Desktop\cognifyz_2
   ```

2. **Run the main menu:**
   ```bash
   python main.py
   ```

3. **Select a task (0-5):**
   - The interactive menu will guide you through available tasks

## 📋 Task Descriptions

### Task 1: Guessing Game (1-100) 🎮
Guess a random number between 1 and 100.
- **Features:**
  - Computer picks a random number
  - Get hints (too high/too low)
  - Performance rating based on attempts
  - Tracks number of attempts

**Run directly:** `python task_1_guessing_game/guessing_game.py`

---

### Task 2: Number Guesser (Custom Range) 🎮
Guess a number within a custom range you define.
- **Features:**
  - Set custom minimum and maximum values
  - Same guessing mechanics as Task 1
  - Adaptive difficulty
  - Smart feedback system

**Run directly:** `python task_2_custom_guesser/custom_guesser.py`

---

### Task 3: Password Strength Checker 🔐
Analyze and rate password strength.
- **Features:**
  - Checks 7+ security criteria:
    - Length (8, 12, 16 characters)
    - Uppercase letters (A-Z)
    - Lowercase letters (a-z)
    - Numbers (0-9)
    - Special characters (!@#$%^&*)
    - No sequential patterns
    - No repeated characters
  - Real-time feedback and suggestions
  - Strength scoring (Very Weak to Excellent)
  - Interactive mode for multiple checks

**Run directly:** `python task_3_password_checker/password_checker.py`

---

### Task 4: Fibonacci Sequence 📊
Generate and analyze Fibonacci sequences.
- **Features:**
  - Generate first N Fibonacci numbers
  - Generate Fibonacci numbers up to a value
  - Check if a number is Fibonacci
  - Display interesting properties
  - Formatted output with statistics

**Run directly:** `python task_4_fibonacci/fibonacci.py`

**Options in Task 4:**
1. Generate first N numbers
2. Generate up to a maximum value
3. Check if a number is Fibonacci
4. Display properties and facts

---

### Task 5: File Manipulation - Word Count 📄
Analyze text files for statistics.
- **Features:**
  - Count words, lines, characters, file size
  - Analyze multiple files
  - Create and analyze sample files
  - Compare multiple files
  - Formatted statistical reports

**Run directly:** `python task_5_word_count/word_count.py`

**Options in Task 5:**
1. Analyze a single file
2. Analyze all .txt files in a directory
3. Create sample file and analyze
4. Compare multiple files

---

## 🎯 Usage Examples

### Example 1: Run Main Menu
```bash
python main.py
```
Then choose option 1, 2, 3, 4, 5, or 0 (exit)

### Example 2: Run Task Directly
```bash
python task_1_guessing_game/guessing_game.py
```

### Example 3: Windows Batch File (Optional)
Create a file named `run.bat`:
```batch
@echo off
python main.py
pause
```
Then double-click `run.bat` to run.

---

## 💡 Tips

- **Windows Users:** You can drag the project folder to your terminal or use PowerShell
- **Linux/Mac Users:** Use `python3` instead of `python`
- **Exit Anytime:** Press `Ctrl+C` to interrupt and return to menu
- **Interactive Mode:** All tasks run in interactive mode by default

---

## 🔧 Customization

### Modifying Tasks
Each task file is independent and can be modified:
- Change difficulty levels
- Add new features
- Modify output formatting
- Add scoring systems

### Adding New Tasks
1. Create a new folder: `task_X_name/`
2. Create the Python script
3. Update `main.py` to include the new task

---

## 📝 Requirements

- **Python:** 3.6+
- **OS:** Windows, macOS, Linux
- **Dependencies:** None (uses only Python standard library)

---

## 🐛 Troubleshooting

**Issue:** "ModuleNotFoundError" or "No module named"
- **Solution:** Ensure you're in the correct directory and running with Python

**Issue:** "File not found" in Task 5
- **Solution:** Provide absolute paths or ensure files are in the correct directory

**Issue:** Password checker doesn't show all suggestions
- **Solution:** This is normal; only unsatisfied criteria are shown

**Issue:** Permission denied
- **Solution:** Ensure the directory has write permissions for creating sample files

---

## 📊 Sample Output

### Main Menu:
```
==================================================
       COGNIFYZ - TASK SELECTOR
==================================================

=== Level 2 Tasks ===
1. Guessing Game (1-100)
2. Number Guesser (custom range)
3. Password Strength Checker
4. Fibonacci Sequence
5. File Manipulation (word count)
0. Exit

Choose a task to run (0-5):
```

---

## 📧 About

**Project:** COGNIFYZ Level 2 Tasks
**Purpose:** Educational Python programming exercises
**Created:** 2026
**Version:** 1.0

---

## 📄 License

Free to use and modify for educational purposes.

---

## 🎓 Learning Outcomes

By using this project, you'll learn:
- Interactive Python programming
- User input/output handling
- File operations
- String manipulation
- Algorithm implementation
- Function design and organization
- Error handling and validation
- Code structure and modularity

---

## 🚀 Future Enhancements

Possible improvements:
- Add leaderboards for guessing games
- Implement password generator
- Add more Fibonacci properties
- Advanced file analysis (word frequency, etc.)
- Configuration files for customization
- Unit tests

---

Enjoy coding! 🎉
"# Cognifyz_level_2" 
