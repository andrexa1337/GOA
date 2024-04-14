# Define the correct password
correct_password = "password123"

# Prompt the user for a password
while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Correct password entered. Access granted.")
        break  # Exit the loop if the correct password is entered
    else:
        print("Incorrect password. Try again.")
