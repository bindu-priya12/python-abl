
password = input("Enter your password: ")

errors = []

# Check minimum length
if len(password) < 8:
    errors.append("Password must contain at least 8 characters.")

# Check uppercase letter
if not any(ch.isupper() for ch in password):
    errors.append("Password must contain an uppercase letter.")

# Check lowercase letter
if not any(ch.islower() for ch in password):
    errors.append("Password must contain a lowercase letter.")

# Check digit
if not any(ch.isdigit() for ch in password):
    errors.append("Password must contain a digit.")

# Check special character
if not any(not ch.isalnum() for ch in password):
    errors.append("Password must contain a special character.")

# Check consecutive repeated characters
for i in range(len(password) - 2):
    if password[i] == password[i + 1] == password[i + 2]:
        errors.append("Three consecutive identical characters are not allowed.")
        break

# Check prohibited text
lower_password = password.lower()

if "password" in lower_password or "admin" in lower_password:
    errors.append("Password must not contain prohibited text.")

# Display result
if len(errors) == 0:
    print("Valid Password!")
    print("All password rules are satisfied.")
else:
    print("Invalid Password!")
    print("The following rules are not satisfied:")
    for error in errors:
        print("-", error)
