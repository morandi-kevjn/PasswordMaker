import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation + '!@#$%^&*()_+-=[]{}|;:,.<>?'
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    length = int(input("Enter the length of the password: "))
    print("Generated password: ", generate_password(length))


if __name__ == 'main':
    main()
