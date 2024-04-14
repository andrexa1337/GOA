# Ask the user to enter the age of 5 people
age1 = int(input("Enter the age of the first person: "))
age2 = int(input("Enter the age of the second person: "))
age3 = int(input("Enter the age of the third person: "))
age4 = int(input("Enter the age of the fourth person: "))
age5 = int(input("Enter the age of the fifth person: "))

# Calculate the result
result = (age1 * age2) / age3 + (age4 + age5) * (age1 + age2)

# Print the result
print("The result of the calculation is:", result)
