
import random
import string

print("==============================")
print("      PASSWORD GENERATOR")
print("==============================")

while True:

    try:
        length = int(input("\nEnter password length: "))

        if length < 1:
            print("Password length must be at least 1.")
            continue

        # Character collections
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Combine all characters
        all_characters = lowercase + uppercase + digits + symbols

        # Generate password
        password = ''.join(
            random.choice(all_characters)
            for i in range(length)
        )

        print("\nYour generated password is:")
        print(password)

        again = input("\nGenerate another password? (yes/no): ")

        if again.lower() != "yes":
            print("Thank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")
