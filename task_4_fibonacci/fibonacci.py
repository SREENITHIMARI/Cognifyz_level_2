#!/usr/bin/env python3
"""
Task 4: Fibonacci Sequence
Generate and display Fibonacci sequences with different options.
"""

def generate_fibonacci(count):
    """Generate Fibonacci sequence up to count terms"""
    if count <= 0:
        return []
    elif count == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, count):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

def fibonacci_up_to_value(max_value):
    """Generate Fibonacci sequence up to a maximum value"""
    fib_sequence = [0, 1]
    while fib_sequence[-1] < max_value:
        next_val = fib_sequence[-1] + fib_sequence[-2]
        if next_val > max_value:
            break
        fib_sequence.append(next_val)
    
    return [x for x in fib_sequence if x <= max_value]

def is_fibonacci(num):
    """Check if a number is a Fibonacci number"""
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

def fibonacci_menu():
    """Main Fibonacci menu and operations"""
    print("\n" + "=" * 50)
    print("    📊 FIBONACCI SEQUENCE")
    print("=" * 50)
    print("\nChoose an option:")
    print("1. Generate first N Fibonacci numbers")
    print("2. Generate Fibonacci numbers up to a value")
    print("3. Check if a number is Fibonacci")
    print("4. Display Fibonacci properties")
    print("5. Back to main menu")
    print()

def fibonacci_generator():
    """Main Fibonacci function"""
    while True:
        fibonacci_menu()
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '5':
                break
            
            elif choice == '1':
                print()
                n = int(input("How many Fibonacci numbers to generate? "))
                
                if n <= 0:
                    print("❌ Please enter a positive number!\n")
                    continue
                
                fib_seq = generate_fibonacci(n)
                print(f"\n📈 First {n} Fibonacci numbers:")
                print("-" * 50)
                
                # Display in formatted way
                for i, num in enumerate(fib_seq, 1):
                    print(f"F({i:2d}) = {num:>12,d}", end="   ")
                    if i % 3 == 0:
                        print()
                
                if len(fib_seq) % 3 != 0:
                    print()
                
                print(f"\nSum of all: {sum(fib_seq):,}")
                print("-" * 50 + "\n")
            
            elif choice == '2':
                print()
                max_val = int(input("Up to which value? "))
                
                if max_val < 0:
                    print("❌ Please enter a positive number!\n")
                    continue
                
                fib_seq = fibonacci_up_to_value(max_val)
                print(f"\n📈 Fibonacci numbers up to {max_val:,}:")
                print("-" * 50)
                
                for i, num in enumerate(fib_seq, 1):
                    print(f"F({i:2d}) = {num:>12,d}", end="   ")
                    if i % 3 == 0:
                        print()
                
                if len(fib_seq) % 3 != 0:
                    print()
                
                print(f"\nTotal count: {len(fib_seq)}")
                print(f"Sum of all: {sum(fib_seq):,}")
                print("-" * 50 + "\n")
            
            elif choice == '3':
                print()
                num = int(input("Enter a number to check: "))
                
                if is_fibonacci(num):
                    print(f"\n✅ {num:,} is a Fibonacci number!\n")
                else:
                    print(f"\n❌ {num:,} is NOT a Fibonacci number.\n")
            
            elif choice == '4':
                print("\n" + "=" * 50)
                print("📚 FIBONACCI PROPERTIES")
                print("=" * 50)
                print("\n✨ Interesting facts about Fibonacci:")
                print("   • Appears in nature (flowers, shells, spirals)")
                print("   • Related to the Golden Ratio (≈ 1.618)")
                print("   • Each number is sum of previous two")
                print("   • F(n) = F(n-1) + F(n-2)")
                print("   • Found in art, architecture, and biology")
                print("\n🔢 First 20 Fibonacci numbers:")
                print("-" * 50)
                
                fib_seq = generate_fibonacci(20)
                for i, num in enumerate(fib_seq, 1):
                    print(f"F({i:2d}) = {num:>12,d}", end="   ")
                    if i % 3 == 0:
                        print()
                
                print("\n" + "=" * 50 + "\n")
            
            else:
                print("❌ Invalid choice! Please enter 1-5.\n")
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted!")
            break

if __name__ == "__main__":
    try:
        fibonacci_generator()
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted!")
