
"""
Hard-code a username and password.

Ask the user to enter them.

Print:

"Login successful!" if both match

"Invalid username or password" otherwise

"""
import getpass # a built-in module by Python that hides the text being typed on screen
import time 

max_attempts = 3
attempts = 0


# hard-coded username and password: test
"""correct_username = "Tyrese"
correct_password = "123456"""

#  the following is a directory that stores hard-coded username and password in key-valued pairs
# key --> usernames : values --> passwords
users = {
    "tyrese": "123456",
    "alice": "password123",
    "thai": "Python12_Cat"
}

while True:
    print("\n" + "="*30)
    action = input("Do you want to login or register? (login/register): ").lower() # new variable that asks if the user wants to LOGIN or Register

    if action == "login": # runs if the condition is TRUE
        logged_in = True


        while attempts < max_attempts: # a loop that iterates until it reaches the max attempts
            print("****      LOGIN PORTAL     ****\n")
            username = input("Enter username: ").lower()

            if username in users: # checks to see if username exists in the directory: if --true-- then ...
                password = getpass.getpass("Enter password: ")

                if password == users[username]: # checks to see the password entered matches up with password in the directory associated with key-valued pair: if --true-- then

                    print("\nLogging in...\n")

                    time.sleep(2) # adds a delay until the next message pops up

                    print("Login Success\n")
                     # exit the loop once the login is successful 
                    
                    while logged_in:
                        print("\nACCOUNT MENU:")
                        print("1. Logout")
                        print("2. Delete Account")

                        menu = input("Enter Option: ").strip()

                        if menu == "1":
                            print(f"{username} signed out.", end="\n")

                            logged_in = False

                        elif menu == "2":
                            account_deletion = input("Enter your username to delete: ").strip().lower()

                            if account_deletion in users:
                                password = getpass.getpass("Enter password to Delete: ")

                                if password == users[account_deletion]:

                                    del users[account_deletion]
                                    print("\nDeleting...\n")

                                    time.sleep(2)

                                    print("Account has been deleted\n")
                        
                                    logged_in = False


                else:
                    attempts += 1 # increments the number of attempts whenever the user inputs incorrect username or password
                    remaining_attempts = max_attempts - attempts
                    print(f"Incorrect credentials. Remaining Attempts {remaining_attempts}\n")
                    
            else:
                print("Username not found. Please try again\n")
        break
                
    elif action == "register":

        print("\n" + "="*30)
        
        
        while True: # loops until gives a username that's not in use.
            print("****      REGISTER PORTAL      ****\n")

            new_username = input("Choose a username: ").lower()

            if new_username in users:
                print("Username already in use. Choose another one")
            
            else:
                new_password = getpass.getpass("Enter a password: ")

                users[new_username] = new_password

                print("Registration Successful!\n")
                break

# after exiting the following if statement is ran
if attempts == max_attempts:
    print("User is Blocked")
