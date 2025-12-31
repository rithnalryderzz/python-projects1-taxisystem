mport re

password = input("Enter a password to check: ")

strength = 0

if len(password) >= 8:
    strength += 1
if re.search("[A-Z]", password):
    strength += 1
if re.search("[a-z]", password):
    strength += 1
if re.search("[0-9]", password):
    strength += 1
if re.search("[!@#$%^&*]", password):
    strength += 1

if strength <= 2:
    print("❌ Weak password")
elif strength <= 4:
    print("⚠️ Medium strength password")
else:
    print("✅ Strong password")
