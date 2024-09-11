import random
import string

def generate_password(length, complex):
    """
    Generate a password of the length and complexity which is specified.

    """
    if complex == 'low':
        chars = string.ascii_lowercase
    elif complex == 'medium':
        chars = string.ascii_letters + string.digits
    elif complex == 'high':
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid level of complexity")

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("__________________")

    # Ask the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter desired length of the password: "))
            if length < 8:
                print("Password should be of at least 8 characters.")
                continue
            break
        except ValueError:
            print("Invalid input!! Pleaseee enter a positive integer.")

    # Ask the user to specify the complexity of the password
    while True:
        complex = input("Enter the complexity of the password (low, medium, high): ")
        if complex in ['low', 'medium', 'high']:
            break
        print("Invalid input!! Please select low, medium, or high.")

    # Generate and display the password on screen
    password = generate_password(length, complex)
    print("Generated Random Password:")
    print(password)

if __name__ == "__main__":
    main()