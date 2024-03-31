import random
import string

def generate_password(length=12, include_numbers=True, include_symbols=True):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    password = generate_password(length, include_numbers, include_symbols)
    print("Generated Password:", password)

if _name_ == "_main_":
    main()