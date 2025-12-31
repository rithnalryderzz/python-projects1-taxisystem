import re

password = input("Enter a password to check: ")

issues = []

if len(password) < 8:
    issues.append("Password should be at least 8 characters long")
if not re.search("[A-Z]", password):
    issues.append("Add at least one uppercase letter")
if not re.search("[a-z]", password):
    issues.append("Add at least one lowercase letter")
if not re.search("[0-9]", password):
    issues.append("Add at least one number")
if not re.search("[!@#$%^&*]", password):
    issues.append("Add at least one special character")

if not issues:
    print("✅ Strong password")
else:
    print("❌ Weak password")
    print("\nSuggestions to improve your password:")
    for issue in issues:
        print("-", issue)
