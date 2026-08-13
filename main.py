#!/usr/bin/env python3
"""
Main menu system for running different tasks
"""
import subprocess
import sys
import os

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """Display the main menu"""
    print("=" * 50)
    print("       COGNIFYZ - TASK SELECTOR")
    print("=" * 50)
    print()
    print("=== Level 2 Tasks ===")
    print("1. Guessing Game (1-100)")
    print("2. Number Guesser (custom range)")
    print("3. Password Strength Checker")
    print("4. Fibonacci Sequence")
    print("5. File Manipulation (word count)")
    print("0. Exit")
    print()

def run_task(task_number):
    """Run the selected task"""
    tasks = {
        1: ("task_1_guessing_game", "guessing_game.py"),
        2: ("task_2_custom_guesser", "custom_guesser.py"),
        3: ("task_3_password_checker", "password_checker.py"),
        4: ("task_4_fibonacci", "fibonacci.py"),
        5: ("task_5_word_count", "word_count.py"),
    }
    
    if task_number not in tasks:
        print("\n❌ Invalid choice! Please select 0-5.")
        input("Press Enter to continue...")
        return False
    
    folder, script = tasks[task_number]
    script_path = os.path.join(folder, script)
    
    if not os.path.exists(script_path):
        print(f"\n❌ Error: {script_path} not found!")
        input("Press Enter to continue...")
        return False
    
    print(f"\n🚀 Running {folder}...\n")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, script_path])
    except KeyboardInterrupt:
        print("\n\n⚠️  Task interrupted by user.")
    except Exception as e:
        print(f"\n❌ Error running task: {e}")
    
    print("-" * 50)
    input("\nPress Enter to return to menu...")
    return True

def main():
    """Main menu loop"""
    while True:
        clear_screen()
        print_menu()
        
        try:
            choice = input("Choose a task to run (0-5): ").strip()
            
            if choice == '0':
                print("\n👋 Thank you for using COGNIFYZ! Goodbye!\n")
                sys.exit(0)
            
            task_num = int(choice)
            if run_task(task_num):
                pass
            
        except ValueError:
            print("\n❌ Invalid input! Please enter a number between 0-5.")
            input("Press Enter to continue...")
        except KeyboardInterrupt:
            print("\n\n👋 Exiting... Goodbye!\n")
            sys.exit(0)

if __name__ == "__main__":
    main()
