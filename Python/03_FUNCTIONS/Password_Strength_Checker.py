def is_strong_password(password):
    """This functions checks if the password is strong or not."""
    
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '@#$%&*?' for char in password):
        return False
    
    return True
password = input("Verify Password : ")
if is_strong_password(password):
    print("Strong Password")
else:
    print("Weak Password")    
    