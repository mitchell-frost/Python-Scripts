# Name of the Program / Person

import random # importing the random package in the program

print("Printing a String") # Printing a string

print("Printing an integer : ", 45) # Printing an integer

intValue = input("Enter an string number to convert to integer: ")
intValue = int(intValue) # string to integer conversion
print("The string converted to integer is ", intValue)

x = input("Enter a value : ") # input statement

n = random.random() # generating a random number
n = n * 100
print("A random number is : ", n) # printing the random number generated

print("For loop to print the first ten numbers")
for i in range(10):
	print(i)

# comment right after the for loop :
# It increments the value of i by 1 and goes till 10
# It prints the value in every iteration

print("While loop to print first 10 odd numbers")
i = 1 # initialising value of i to 1
while True: # the loop works till it is True, i.e, if we don't break the loop, it will become an infinite loop
	print(i) # prints the value of i in every iteration
	i += 2 # increases the value of i by 2
	if (i > 20): # checks the condition of i is greater than 20
		break # break statement in the while loop that breaks the loop when i becomes greater than 20

# The while loop works till it is true, which means, it is an infinite loop. It prints the value of i in every iteration. 
# The value of i is incremented by 2 in every iteration of the loop. If the value of i becomes greater than 20,
# The control reaches the break statement and breaks out of the loop.

even_odd = input("Enter a number to check if it is even or odd : ") # initialising variable to 45
even_odd = int(even_odd) # converting to integer because all input is in string in python
if (even_odd % 2 == 0): # the condition checks if the variable even_odd is divisible by 2.
	print(even_odd, "is an even number. \n") # prints this if the variable is even
else:
	print(even_odd, "is an odd number. \n") # prints this if the variable is odd

strName = 'Your Name Here' # initialising variable with a string value
if (strName == 'Your Name Here'): # if statement with string condition
	print("Your name is : ", strName, "\n") # printing the value of string

num = input("Enter a number to check if it is > 20 or < 100 : ")
num = int(num) # converting to integer because all input is in string in python
if (num > 20 and num < 100): # if statement with AND (boolean) condition
	print(num, "is greater than 20 and less than 100 \n") # prints the value of num 

# the if statement checks if the value of num is greater than 20 AND less than 100
# and prints it's value if it satisfies both of the conditions

num = input("Enter a number to check if it is > 50 or < 100 : ")
num = int(num) # converting to integer because all input is in string in python
if (num > 50 or num < 100): # if statement with OR (boolean) condition
	print(num, "satisfies one of the two conditions, > 50 or < 100 \n") 

# the if statement checks if the value of num is greater than 50 OR less than 100
# and prints it's value if it satisfies one of the two conditions

num = input("Enter a number to check if it is > 50 or > 30 or neither : ")
num = int(num) # converting to integer because all input is in string in python
if (num > 50):
	print(num, "is greater than 50 \n") # prints this if it is greater than 50
elif (num > 30): # elif statement
	print(num, "is greater than 30 \n") # prints this if it is greater than 30
else: # else statement
	print(num, "is not greater than 50 or 30 \n") # prints this if it is neither of the two

# the program asks for user input
# it then checks if the number is greater than 50
# or if it is greater than 30 with the elif statement
# it then goes to else block and then prints the last line