import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    # Initialize an empty list to store possible characters
    character_pool = ''
    
    # Add character sets based on user preferences
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_digits:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation

    # Ensure at least one character type is selected
    if not character_pool:
        raise ValueError("At least one character type must be selected.")
    
    # Generate the password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    # Prompt user for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 8): "))
            if length < 8:
                print("Password length should be at least 8. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Prompt user for character type preferences
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate and display the password
    try:
        password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
