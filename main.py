
"""
Hard-code a username and password.

Ask the user to enter them.

Print:

"Login successful!" if both match

"Invalid username or password" otherwise

"""

max_attempts = 3
attempts = 0


# hard-coded username and password
correct_username = "Tyrese"
correct_password = "123456"



while attempts < max_attempts: # a loop that iterates until it reaches the max attempts

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")

        break # exit the loop once the login is successful 

    else:
        attempts += 1 # increments the number of attempts whenever the user inputs incorrect username or password
        remaining_attempts = max_attempts - attempts
        print(f"Incorrect credentials. Remaining Attempts {remaining_attempts}")

# after exiting the following if statement is ran
if attempts == max_attempts:
    print("User is Blocked")
