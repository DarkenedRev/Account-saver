import random
import string
import os
import webbrowser

ACCOUNTS_FILE = "accounts.txt"
PASS_FILE = "pass.txt"  # File where password will be stored

# Password prompt function
def password_check():
    if os.path.exists(PASS_FILE):
        with open(PASS_FILE, "r") as f:
            stored_password = f.read().strip()
        
        if stored_password == "SEXWAREUD":
            print("You are now logged in. Have fun!")
            return True  # Auto login successful
        else:
            print("Stored password is incorrect or empty. Please provide the correct password.")
    
    correct_password = "SEXWAREUD"
    attempts = 0
    while attempts < 3:  # Allow up to 3 attempts
        password = input("What's the password: ")
        if password == correct_password:
            print("Password correct! Access granted.")
            with open(PASS_FILE, "w") as f:
                f.write(correct_password)  # Save the correct password for future logins
            return True
        else:
            attempts += 1
            print("Incorrect password. Try again.")
    
    print("Too many incorrect attempts. Exiting...")
    exit()  # Exit the program after 3 failed attempts

# Random password generator
def generate_random_password():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(12))
    print(f"Generated password: {password}")
    wait_for_main()

def store_account():
    try:
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        description = input("Enter description: ")
        
        if not username or not email or not password or not description:
            print("All fields are required! Please fill in all fields.")
            return

        with open(ACCOUNTS_FILE, "a") as f:
            f.write(f"Username: {username}\nEmail: {email}\nPassword: {password}\nDescription: {description}\n---\n")
        
        print("Account stored successfully!")
    except Exception as e:
        print(f"An error occurred while storing the account: {e}")
    wait_for_main()

def view_accounts():
    try:
        if os.path.exists(ACCOUNTS_FILE):
            with open(ACCOUNTS_FILE, "r") as f:
                accounts_data = f.read()
            
            if accounts_data:
                accounts = accounts_data.split("\n---\n")
                print("Select an account to view:\n")
                
                for i, account in enumerate(accounts, 1):
                    username = account.split("\n")[0].replace("Username: ", "")
                    print(f"{i}: {username}")
                
                account_choice = input("Enter the number of the account: ")
                
                try:
                    account_index = int(account_choice) - 1
                    if 0 <= account_index < len(accounts):
                        print(f"\nDetails of selected account:\n{accounts[account_index]}")
                    else:
                        print("Invalid choice. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                print("No accounts stored yet.")
        else:
            print(f"{ACCOUNTS_FILE} not found.")
    except Exception as e:
        print(f"An error occurred while viewing the accounts: {e}")
    wait_for_main()

def delete_account():
    try:
        if os.path.exists(ACCOUNTS_FILE):
            with open(ACCOUNTS_FILE, "r") as f:
                accounts_data = f.read()
            
            if accounts_data:
                accounts = accounts_data.split("\n---\n")
                print("Select an account to delete:\n")
                
                for i, account in enumerate(accounts, 1):
                    username = account.split("\n")[0].replace("Username: ", "")
                    print(f"{i}: {username}")
                
                account_choice = input("Enter the number of the account to delete: ")
                
                try:
                    account_index = int(account_choice) - 1
                    if 0 <= account_index < len(accounts):
                        del accounts[account_index]

                        with open(ACCOUNTS_FILE, "w") as f:
                            f.write("\n---\n".join(accounts))

                        print("Account deleted successfully!")
                    else:
                        print("Invalid choice. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                print("No accounts stored yet.")
        else:
            print(f"{ACCOUNTS_FILE} not found.")
    except Exception as e:
        print(f"An error occurred while deleting the account: {e}")
    wait_for_main()

def open_discord():
    webbrowser.open("https://discord.com/invite/KkNeWQPqX5")
    wait_for_main()

def open_lego_signup():
    webbrowser.open("https://identity.lego.com/en-US/register?")
    wait_for_main()

def link_lego_to_epic():
    webbrowser.open("https://www.epicgames.com/account/connections?")
    wait_for_main()

def wait_for_main():
    input("Press M to return to the main menu.")
    main_menu(False)

def main_menu(show_banner=True):
    os.system("cls" if os.name == "nt" else "clear")
    if show_banner:
        print("SEXWARE Account Manager v1.3")

    print(""" 
    1: Epic Games Signup       2: Temp Mail Website       3: Generate Password
    4: Store Account           5: View Account            6: Edit Account
    7: Delete Account          8: Sexware Discord         9: LEGO Account Signup
    10: Link LEGO to Epic      11: Exit
    """)

    choice = input("Enter the number of your choice: ")
    if choice == "1":
        webbrowser.open("https://www.epicgames.com/id/register/date-of-birth")
        wait_for_main()
    elif choice == "2":
        webbrowser.open("https://temp-mail.org/en/")
        wait_for_main()
    elif choice == "3":
        generate_random_password()
    elif choice == "4":
        store_account()
    elif choice == "5":
        view_accounts()
    elif choice == "6":
        delete_account()
    elif choice == "7":
        delete_account()
    elif choice == "8":
        open_discord()
    elif choice == "9":
        open_lego_signup()
    elif choice == "10":
        link_lego_to_epic()
    elif choice == "11":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Try again.")
        main_menu(False)

if __name__ == "__main__":
    if password_check():
        main_menu()
