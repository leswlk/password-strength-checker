import re

def check_password_strength(password):
    # Define the reasons for password strength checks
    checks = {
        "Password is too short. It should be at least 8 characters long.": len(password) < 8,
        "Password should have at least one lowercase letter.": not re.search("[a-z]", password),
        "Password should have at least one uppercase letter.": not re.search("[A-Z]", password),
        "Password should have at least one digit.": not re.search("[0-9]", password),
        "Password should have at least one special character.": not re.search("[!@#$%^&*(),.?\":{}|<>]", password)
    }
    
    reasons = [message for message, failed in checks.items() if failed]

    # Early return if no reasons are found
    if not reasons:
        return "Congratulations! Your password is strong!"
    
    return "Weak: " + " , ".join(reasons)

def main():
    print("Welcome to PasswordStrengthChecker!")
    while True:
        password = input("Please enter a password for testing: ")
        print(f"You entered: {password}")  # Debugging line
        strength_result = check_password_strength(password)
        print(strength_result)

        # Check if the password is strong
        if "Congratulations!" in strength_result:
            break  # Exit the loop if the password is strong

if __name__ == "__main__":
    main()

