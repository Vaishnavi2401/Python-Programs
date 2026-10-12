# Password checker Code

def password_checker(password):
    '''
    Strong password  -->
    1. length should be grater then 8
    2. should contain alteast 1 lowercase character
    3. should contain alteast 1 uppercase character
    4. should have atleast 1 digit
    5. should have ateast 1 special character  
    '''
    if(len(password) < 8):
        print("Your password is a weak password")

    elif not any(char.islower() for char in password):
        print("Your password is a weak password")

    elif not any(char.isupper() for char in password):
        print("Your password is a weak password")

    elif not any(char.isdigit() for char in password):
        print("Your password is a weak password")

    elif not any(char for char in '!@#$%^&*()_-+=|<>.?,/' for char in password):
        print("Your password is a weak password")

    else:
        print("Your password is strong password")

input_password = input("Enter your password:")

password_checker(input_password)
