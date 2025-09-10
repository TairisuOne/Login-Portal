
"""
Hard-code a username and password.

Ask the user to enter them.

Print:

"Login successful!" if both match

"Invalid username or password" otherwise

"""
import getpass # a built-in module by Python that hides the text being typed on screen

max_attempts = 3
attempts = 0


# hard-coded username and password: test
"""correct_username = "Tyrese"
correct_password = "123456"""

#  the following is a directory that stores hard-coded username and password in key-valued pairs
# key --> usernames : values --> passwords
users = {
    "Tyrese": "123456",
    "Alice": "password123",
    "Thai": "Python12_Cat"
}


action = input("Do you want to login or register? (login/register): ").lower() # new variable that asks if the user wants to LOGIN or Register

if action == "login": # runs if the condition is TRUE

    while attempts < max_attempts: # a loop that iterates until it reaches the max attempts

        username = input("Enter username: ")

        if username in users: # checks to see if username exists in the directory: if --true-- then ...
            password = getpass.getpass("Enter password: ")

            if password == users[username]: # checks to see the password entered matches up with password in the directory associated with key-valued pair: if --true-- then

                print("Login Success")
                break # exit the loop once the login is successful 
            
            else:
                attempts += 1 # increments the number of attempts whenever the user inputs incorrect username or password
                remaining_attempts = max_attempts - attempts
                print(f"Incorrect credentials. Remaining Attempts {remaining_attempts}")
                
        if username not in users:
            print("Username not found. Please try again")

            
elif action == "register":

    while True: # loops until gives a username that's not in use.
        new_username = input("Choose a username: ")

        if new_username in users:
            print("Username already in use. Choose another one")
        
        else:
            new_password = getpass.getpass("Enter a password: ")

            users[new_username] = new_password

            print("Registration Successful!")
            break


# after exiting the following if statement is ran
if attempts == max_attempts:
    print("User is Blocked")
