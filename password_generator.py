import random
import string

print("🔑 Secure Password Generator")

while True:
    try:
        length = int(input("Enter desired password length (minimum 8): "))
        if length < 8:
            print("Password length must be at least 8.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

# Required characters
uppercase = random.choice(string.ascii_uppercase)
lowercase = random.choice(string.ascii_lowercase)
digit = random.choice(string.digits)
symbol = random.choice("!@#$%^&*")

# Remaining characters
remaining_length = length - 4
all_characters = string.ascii_letters + string.digits + "!@#$%^&*"
remaining = [random.choice(all_characters) for _ in range(remaining_length)]

# Combine and shuffle
password_list = [uppercase, lowercase, digit, symbol] + remaining
random.shuffle(password_list)

password = "".join(password_list)

print("\n✅ Generated Secure Password:")
print(password)
