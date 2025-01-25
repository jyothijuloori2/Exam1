def check_strength(password):
    if len(password)<8:
        return "Your password must contain atleast  8 characters"
    has_upper=False
    has_lower=False
    has_digit=False
    has_special=False
    for char in password:
        if char.isupper():
            has_upper=True
        elif char.islower():
            has_lower=True
        elif char.isdigit():
            has_digit=True
        elif not char.isalnum():
            has_special=True
    if not has_upper:
        return "your must contain atleast one upper character"
    elif not has_lower:
        return "your must contain atleast one lower character"
    elif not has_digit:
        return "your must contain atleast one digit"
    elif not has_special:
        return "your must contain atleast one special character"
    return "password is strong"
def main():
    password=input("enter a password:")
    result=check_strength(password)
    print(result)
    
main()