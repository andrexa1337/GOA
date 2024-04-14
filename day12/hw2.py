# Ask the user to enter a number
number = int(input("Enter a number: "))

# Validate the input to ensure it's a positive integer
while number <= 0:
    print("Please enter a positive integer.")
    number = int(input("Enter a number: "))

# Count down from the entered number to 1
print("Counting down from", number, "to 1:")
while number >= 1:
    print(number)
    number -= 1
