import re

COMMON_PASSWORDS = ["password", "123456", "qwerty", "admin", "letmein", "welcome"]

def check_password_strength(password):
    # Minimum length requirement
    if len(password) < 8:
        return "Password is too short. It must be at least 8 characters long."

    # Check for common passwords
    if password.lower() in COMMON_PASSWORDS:
        return "Password is commonly used. Choose a more secure password."

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."

    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."

    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."

    # Check for at least one special character
    special_characters = re.compile(r"[!@#$%^&*(),.?\":{}|<>]")
    if not special_characters.search(password):
        return "Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>)."

    # Password meets all criteria
    return "Password is strong and meets all requirements."

# Continuously prompt the user until they enter a strong password
while True:
    # Get a password from the user
    password = input("Enter your password: ")

    # Check the password strength
    result = check_password_strength(password)

    # Display the result
    print(result)

    # If the password is strong, exit the loop
    if "strong" in result.lower():
        break
