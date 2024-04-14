# Ask the user to enter a positive integer
num = int(input("Enter a positive integer: "))

# Validate the input to ensure it's a positive integer
while num <= 0:
    print("Please enter a positive integer.")
    num = int(input("Enter a positive integer: "))

# Calculate the sum of all numbers from 1 to num
sum_of_numbers = 0
for i in range(1, num + 1):
    sum_of_numbers += i

# Print the sum of all numbers from 1 to num
print("The sum of all numbers from 1 to", num, "is:", sum_of_numbers)
