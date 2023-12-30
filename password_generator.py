import random
import string

def generate_strong_password(length=12):
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure the password length is at least 8 characters
    length = max(12, length)

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def generate_and_save_passwords(file_path, num_passwords=100000):
    # Generate passwords
    passwords = [generate_strong_password() for _ in range(num_passwords)]

    # Write passwords to a text file
    with open(file_path, 'a') as file:
        for password in passwords:
            file.write(password + '\n')

# Example usage:
file_path = 'dict.txt'
generate_and_save_passwords(file_path)

print(f"Passwords have been generated and saved to '{file_path}'.")
