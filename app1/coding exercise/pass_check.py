def check_password_strength(password):
    if len(password) < 8:
        return "weak password"
    elif not any(i.isupper() for i in password):
        return "weak password"
    elif not any(i.isdigit() for i in password):
        return "weak password"
    else:
        return "strong password"


password = input("Enter a new password: ")
print(check_password_strength(password))
