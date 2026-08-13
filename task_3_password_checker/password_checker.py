#!/usr/bin/env python3
"""
Task 3: Password Strength Checker
Checks and rates the strength of a password based on various criteria.
"""
import re

def check_password_strength(password):
    """
    Check password strength and return score and feedback
    Returns: (score, strength_level, feedback_list)
    """
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")
    
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("⚠️  Consider using at least 12 characters for better security")
    
    if len(password) >= 16:
        score += 1
    
    # Lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters (a-z)")
    
    # Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters (A-Z)")
    
    # Numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add numbers (0-9)")
    
    # Special characters
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        score += 1
    else:
        feedback.append("❌ Add special characters (!@#$%^&*)")
    
    # Check for common patterns
    if re.search(r'(.)\1{2,}', password):  # Repeated characters
        score -= 1
        feedback.append("⚠️  Avoid repeating characters")
    
    if re.search(r'(012|123|234|345|456|567|678|789|890|abc|bcd|cde)', password.lower()):
        score -= 1
        feedback.append("⚠️  Avoid sequential patterns")
    
    # Determine strength level
    if score <= 2:
        strength = "🔴 Very Weak"
    elif score <= 4:
        strength = "🟠 Weak"
    elif score <= 6:
        strength = "🟡 Fair"
    elif score <= 8:
        strength = "🟢 Good"
    else:
        strength = "🟢🟢 Excellent"
    
    return max(0, score), strength, feedback

def password_checker():
    """Main password checker function"""
    print("\n" + "=" * 60)
    print("    🔐 PASSWORD STRENGTH CHECKER")
    print("=" * 60)
    print("\nEnter passwords to check their strength.")
    print("Type 'quit' to exit.\n")
    
    while True:
        password = input("Enter a password to check: ")
        
        if password.lower() == 'quit':
            print("\n👋 Goodbye!\n")
            break
        
        if not password:
            print("❌ Please enter a password!\n")
            continue
        
        score, strength, feedback = check_password_strength(password)
        
        print("\n" + "-" * 60)
        print(f"Password Length: {len(password)} characters")
        print(f"Strength Score: {score}/9")
        print(f"Strength Level: {strength}")
        print("\n📋 Criteria Check:")
        
        # Show what was satisfied
        criteria = [
            ("✅ At least 8 characters", len(password) >= 8),
            ("✅ At least 12 characters", len(password) >= 12),
            ("✅ At least 16 characters", len(password) >= 16),
            ("✅ Lowercase letters (a-z)", bool(re.search(r'[a-z]', password))),
            ("✅ Uppercase letters (A-Z)", bool(re.search(r'[A-Z]', password))),
            ("✅ Numbers (0-9)", bool(re.search(r'[0-9]', password))),
            ("✅ Special characters", bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password))),
        ]
        
        for criterion, satisfied in criteria:
            if satisfied:
                print(criterion)
        
        if feedback:
            print("\n💡 Suggestions:")
            for suggestion in feedback:
                print(suggestion)
        
        print("-" * 60 + "\n")

if __name__ == "__main__":
    try:
        password_checker()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted!")
