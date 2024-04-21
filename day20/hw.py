print("Multiples of 5 and 3 from 1 to 100:")
for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print(i, end=" ")


name_list = []
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
name_list.append(first_name)
name_list.append(last_name)
print("Final list:", name_list)


num = int(input("Enter a number: "))
numbers = list(range(1, num + 1))
print("Numbers from 1 to", num, ":", numbers)
print("Sum:", sum(numbers))
print("Arithmetic mean:", sum(numbers) / len(numbers))


even_numbers = []
for i in range(2, 51, 2):
    even_numbers.append(i)
print("Even numbers from 1 to 50:", even_numbers)


number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is not even")


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result_list = []
for num in range(a, b):
    result_list.append(num)
print("Numbers between", a, "and", b, ":", result_list)



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
reversed_list = my_list[::-1]
print("Reversed list:", reversed_list)
