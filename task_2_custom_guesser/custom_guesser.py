#!/usr/bin/env python3
"""
Task 2: Number Guesser (Custom Range)
Player sets custom min/max range and tries to guess the number.
"""
import random

def custom_guesser():
    """Main custom number guesser function"""
    print("\n" + "=" * 50)
    print("    🎮 NUMBER GUESSER (CUSTOM RANGE)")
    print("=" * 50)
    print("\nSet your custom range and I'll think of a number!\n")
    
    try:
        while True:
            min_num = int(input("Enter minimum number: "))
            max_num = int(input("Enter maximum number: "))
            
            if min_num >= max_num:
                print("❌ Minimum must be less than maximum! Try again.\n")
                continue
            
            break
        
        print(f"\n✅ I'm thinking of a number between {min_num} and {max_num}.")
        print("Can you guess what it is?\n")
        
        secret_number = random.randint(min_num, max_num)
        attempts = 0
        guessed = False
        
        while not guessed:
            try:
                guess = int(input(f"Enter your guess ({min_num}-{max_num}): "))
                attempts += 1
                
                if guess < min_num or guess > max_num:
                    print(f"❌ Please enter a number between {min_num} and {max_num}!\n")
                    continue
                
                if guess < secret_number:
                    print("📈 Too low! Try a higher number.\n")
                elif guess > secret_number:
                    print("📉 Too high! Try a lower number.\n")
                else:
                    guessed = True
                    print("\n" + "=" * 50)
                    print(f"🎉 Congratulations! You guessed it: {secret_number}")
                    print(f"📊 Total attempts: {attempts}")
                    print(f"🎯 Range was: {min_num} - {max_num}")
                    print("=" * 50)
                    
                    # Congratulate based on attempts
                    range_size = max_num - min_num
                    if attempts <= 5:
                        print("⭐ Amazing! You're a master guesser!")
                    elif attempts <= range_size // 4:
                        print("👍 Great job! That was pretty good!")
                    else:
                        print("💪 Good effort! Practice makes perfect!")
                    print()
                    
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.\n")
    
    except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")
    except KeyboardInterrupt:
        print("\n\n⚠️  Game interrupted!")

if __name__ == "__main__":
    custom_guesser()
