# Password Strength Checker

A robust Python utility for validating password strength based on common security criteria. This tool helps ensure passwords meet basic security requirements by checking for length, character variety, and complexity.

## Features

* Minimum length validation (8 characters)
* Character type requirements:
  * Lowercase letters
  * Uppercase letters
  * Numbers
  * Special characters
* Real-time feedback on password strength
* Interactive command-line interface
* Clear error messages for failed criteria

## Installation

No external dependencies are required. The script uses only Python's built-in `re` module for regular expression operations.

To use this tool, simply download the `password_checker.py` file to your local machine.

## Usage

Run the script from the command line:

```
python password_checker.py
```

The program will:
1. Prompt you to enter a password
2. Analyze the password against security criteria
3. Provide immediate feedback on the password's strength
4. Continue prompting until a strong password is entered

### Example Output

```
Welcome to PasswordStrengthChecker!
Please enter a password for testing: password123
You entered: password123
Weak: Password should have at least one uppercase letter, Password should have at least one special character.

Please enter a password for testing: Password123!
You entered: Password123!
Congratulations! Your password is strong!
```

## Code Structure

### Main Components

1. `check_password_strength(password)`:
   * Core function that evaluates password strength
   * Uses a dictionary to map failure conditions to user-friendly messages
   * Returns either a success message or a list of failing criteria

2. `main()`:
   * Handles the interactive command-line interface
   * Provides continuous password checking until a strong password is entered

### Design Decisions

1. **Dictionary-based Validation**:
   * Uses a dictionary to store validation rules and their corresponding error messages
   * Makes the code more maintainable and easier to modify
   * Allows for simple addition or modification of validation rules

2. **Regular Expressions**:
   * Utilizes Python's `re` module for efficient pattern matching
   * Provides clear and concise way to check for character types
   * Makes the code more readable and maintainable

3. **Early Return Pattern**:
   * Implements early return for valid passwords
   * Reduces code complexity and improves readability
   * Makes the success path clear and distinct

4. **Interactive Loop**:
   * Continues until a strong password is entered
   * Provides immediate feedback for each attempt
   * Creates a user-friendly experience for password testing

## Security Considerations

While this tool provides basic password strength checking, it should not be used as the sole method for password validation in production systems. Consider these additional security measures:

* Implement password hashing
* Add rate limiting for password attempts
* Check against common password databases
* Implement maximum length restrictions
* Add protection against SQL injection and other attacks

## Contributing

Feel free to submit issues and enhancement requests. These basic password requirements can be easily extended by modifying the `checks` dictionary in the `check_password_strength` function.

## License

This project is available under the MIT License. Feel free to use and modify as needed.
