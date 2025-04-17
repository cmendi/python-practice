import getpass

MAX_ATTEMPTS = 3


# get new login info
def get_user_input(prompt):
    while True:
        value = input(prompt)
        if len(value) < MAX_ATTEMPTS:
            print('This field needs to be 3 or more chacters long, please try again.')
        else:
            return value


def get_password_input(prompt):
    while True:
        value = getpass.getpass(prompt)
        if len(value) < MAX_ATTEMPTS:
            print('This field needs to be 3 or more chacters long, please try again.')
        else:
            return value


# new password confirmation
def check_password(password, original_password):
    while True:
        pass_attempts = MAX_ATTEMPTS
        while pass_attempts > 0:
            value = getpass.getpass(password)
            if value != original_password:
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
    failed_attempts = MAX_ATTEMPTS
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
def register():
    new_user = get_user_input('New Username: ')
    new_password = get_password_input('New Password: ')
    confirm_password = check_password('Confirm Password: ', new_password)

    if confirm_password is False:
        return None, None
    return new_user, new_password


while True:
    new_user, new_password = register()

    if not new_user:
        try_again = input('Do you want to try again? (yes/no): ').lower()
        if try_again != 'yes':
            print("Goodbye!")
            exit()
    else:
        break

while True:
    success = login(new_user, new_password)

    if success:
        break
    else:
        try_again = input(
            'Do you want to try logging in again? (yes/no): ').lower()
        if try_again != 'yes':
            print("Goodbye!")
            break
