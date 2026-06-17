import random
import string

print("===== PASSWORD GENERATOR =====")

while True:

    length = int(input("\nEnter password length: "))

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)

    # Strength Check
    if length < 8:
        print("Password Strength: Weak")
    elif length < 12:
        print("Password Strength: Medium")
    else:
        print("Password Strength: Strong")

    choice = input("\nGenerate another password? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank you for using the Password Generator!")
        break
