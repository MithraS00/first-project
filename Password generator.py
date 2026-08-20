import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("Password Generator")
print("------------------")

while True:
    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Please enter a length of at least 4.")
        else:
            break

    except ValueError:
        print("Please enter a number.")


password = generate_password(length)

print("\nYour password is:", password)
