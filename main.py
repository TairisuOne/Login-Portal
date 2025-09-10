
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

while attempts < max_attempts: # a loop that iterates until it reaches the max attempts

    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    if username in users: # checks to see if username exists in the directory

        if password == users[username]: # checks to see the password entered matches up with password in the directory associated with key-valued pair

            print("Login Success")
            break # exit the loop once the login is successful 
        
        else: 
            print("Incorrect Creditentials")
    else:
        attempts += 1 # increments the number of attempts whenever the user inputs incorrect username or password
        remaining_attempts = max_attempts - attempts
        print(f"Incorrect credentials. Remaining Attempts {remaining_attempts}")

# after exiting the following if statement is ran
if attempts == max_attempts:
    print("User is Blocked")
