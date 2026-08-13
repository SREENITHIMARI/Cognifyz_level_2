#!/usr/bin/env python3
"""
Task 1: Guessing Game (1-100)
Player tries to guess a random number between 1 and 100.
"""
import random

def guessing_game():
    """Main guessing game function"""
    print("\n" + "=" * 50)
    print("    🎮 GUESSING GAME (1-100)")
    print("=" * 50)
    print("\nI'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    while not guessed:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("❌ Please enter a number between 1 and 100!\n")
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
                print("=" * 50)
                
                # Congratulate based on attempts
                if attempts <= 5:
                    print("⭐ Amazing! You're a master guesser!")
                elif attempts <= 10:
                    print("👍 Great job! That was pretty good!")
                else:
                    print("💪 Good effort! Practice makes perfect!")
                print()
                
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")

if __name__ == "__main__":
    try:
        guessing_game()
    except KeyboardInterrupt:
        print("\n\n⚠️  Game interrupted!")
