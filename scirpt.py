import getpass

MAX_CHAR = 3

# get new login info


def get_user_input(prompt):
    while True:
        value = input(prompt)
        if len(value) < MAX_CHAR:
            print('This field needs to be 3 or more chacters long, please try again.')
        else:
            return value


def get_password_input(prompt):
    while True:
        value = getpass.getpass(prompt)
        if len(value) < MAX_CHAR:
            print('This field needs to be 3 or more chacters long, please try again.')
        else:
            return value


# new password confirmation
def check_password(password):
    while True:
        pass_attempts = 3
        while pass_attempts > 0:
            value = getpass.getpass(password)
            if value != new_password:
                pass_attempts -= 1
                print(
                    f'Password does not match, you have {pass_attempts} attempts left')
                if pass_attempts == 0:
                    print('To many failed attempts')
                    return False
            else:
                return value


# login function
def login(new_user, new_password):

    # user gets 3 failed attempts
    failed_attempts = 3
    while failed_attempts > 0:
        # User inputs there current user name and password
        current_user = input('Enter username: ')
        current_password = getpass.getpass("Enter Password")

        if current_user == new_user and current_password == new_password:
            print('You are now logged in!')
            return True
        else:
            failed_attempts -= 1
            print(f'Failed login, you have {failed_attempts} attempts left')

            # if user runs out of attempts, they get locked out.
            if failed_attempts == 0:
                print(
                    'To many failed attempts, you are now locked out.')
                return False


# User inputs their new username and password
new_user = get_user_input('Username: ')
new_password = get_password_input('Password: ')
confirm_password = check_password('Confirm Password: ')

while True:
    success = login(new_user, new_password)

    if success:
        break
    else:
        try_again = input('Do you want to try again? (yes/no): ').lower()
        if try_again != 'yes':
            print("Goodbye!")
            break
