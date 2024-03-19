import random
import string

def generate_password(length):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    all_chars = lower_case + upper_case + digits + special_chars
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Invalid length. Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")
        return

    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
