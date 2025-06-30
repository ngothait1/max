import time

print("Hello, this is my final project")

name = input("What is your name? ")
print(f"Hello {name}, nice to meet you")

print("This is a special calculator, I would need two numbers from you")
first_number = int(input("What is your first number? "))
second_number = int(input("What is your second number? "))

print("Thank you for putting in your numbers " + str(first_number) + " and " + str(second_number))
# print(f"Thank you for putting in your numbers {first_number} and {second_number}" )

is_first_odd_or_even = "even"
is_second_odd_or_even = "even"

if first_number % 2 == 1:
    is_first_odd_or_even = "odd"

if second_number % 2 == 1:
    is_second_odd_or_even = "odd"

print("I can see that the first number is " + is_first_odd_or_even)
print("And the second number is " + is_second_odd_or_even)
print("So one of numbers is " + is_first_odd_or_even + " and the second number is " + is_second_odd_or_even)

operator = input("choose an operator - (+, - , * , /): ")

if operator == "+":
    answer = int(first_number) + int(second_number)
    print(str(first_number) + " + " + str(second_number) + " = " + str(answer))

elif operator == "-":
    answer = int(first_number) - int(second_number)
    print(str(first_number) + " - " + str(second_number) + " = " + str(answer))

elif operator == "*":
    answer = int(first_number) * int(second_number)
    print(str(first_number) + " * " + str(second_number) + " = " + str(answer))

elif operator == "/":
    is_integer = input("You choose division, should the result be integer? (y/n) ")
    if second_number == 0:
        print("You can not divide by zero please try again")
    else:
        if is_integer == "y":
            answer = int(first_number) // int(second_number)
        else:
            answer = int(first_number) / int(second_number)

        print(str(first_number) + " / " + str(second_number) + " = " + str(answer))

else:
    print("Operator " + operator + " not valid, please try again.")

print("Thank you " + name + " for using calculator on " + time.ctime())



