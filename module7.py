def check_password(password):
    # Check if password has at least eight characters
    if len(password) < 8:
        return "Invalid Password: Password must have at least eight characters."

    # Check if password consists of only letters and digits
    if not password.isalnum():
        return "Invalid Password: Password must consist of only letters and digits."

    # Count the number of digits in the password
    digit_count = sum(1 for char in password if char.isdigit())

    # Check if password contains at least two digits
    if digit_count < 2:
        return "Invalid Password: Password must contain at least two digits."

    # If all checks pass, the password is valid
    return "Valid Password"


# Prompt the user to enter a password
user_password = input("Enter a password: ")

# Check and display the result
result = check_password(user_password)
print(result)