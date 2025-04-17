import getpass
import time
import datetime

# Configuration
MAX_ATTEMPTS = 3
DELAY_SECONDS = 1

# Utility function for input validation


def get_valid_input(prompt, min_length=3, is_password=False):
    while True:
        # Choose input method
        value = getpass.getpass(prompt) if is_password else input(prompt)
        value = value.strip()
        # Validate length
        if len(value) < min_length:
            print(
                f"This field needs to be at least {min_length} characters long. Please try again.")
        else:
            return value

# Confirm that the user re-entered the same password


def check_password_confirmation(prompt, original_password):
    attempts = MAX_ATTEMPTS
    while attempts > 0:
        confirmed = getpass.getpass(prompt)
        if confirmed != original_password:
            attempts -= 1
            print(
                f"Password does not match, you have {attempts} attempts left.")
            if attempts == 0:
                print("Too many failed attempts.")
                return False
            time.sleep(DELAY_SECONDS)
        else:
            return True
    return False

# Handle user registration (username + password + confirmation)


def register():
    while True:
        username = get_valid_input("Create username: ")
        password = get_valid_input("Create password: ", is_password=True)

        if not check_password_confirmation("Confirm password: ", password):
            retry = input(
                "Registration failed. Try again? (yes/no): ").strip().lower()
            if retry != "yes":
                print("Goodbye!")
                return None, None
        else:
            return username, password

# Handle user login attempts


def login(username, password):
    attempts = MAX_ATTEMPTS
    while attempts > 0:
        current_user = input("Enter username: ")
        current_pwd = getpass.getpass("Enter password: ")

        if current_user == username and current_pwd == password:
            now = datetime.datetime.now()
            formatted = now.strftime('%d/%m/%Y, %H:%M:%S')
            print(f"You are now logged in! (at {formatted})")
            return True
        else:
            attempts -= 1
            print(f"Failed login, you have {attempts} attempts left.")
            if attempts == 0:
                print("Too many failed attempts; you are now locked out.")
                return False
            time.sleep(DELAY_SECONDS)
    return False

# Main application flow


def main():
    # Registration
    username, password = register()
    if not username:
        return

    # Login
    while True:
        if login(username, password):
            break
        retry = input(
            "Do you want to try logging in again? (yes/no): ").strip().lower()
        if retry != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
