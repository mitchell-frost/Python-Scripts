#importing the module
import random

# This is Q1. The function makes a list of 5 passes of the dice
def RollFive():
	list = [random.randint(1, 6) for i in range(5)]
	return list

# this loop calls the function 7 times. It is part of Q1 
#for i in range(7):
#	print(RollFive())

greater_22 = 0 #variable to keep count of the times the sum is greater than 22
less_equal_17 = 0 #variable to keep count of the number of times the sum is less than or equal to 17

#It is part of Q2
for i in range(100):
	sum_of_list = sum(RollFive()) #calling the function to get the list and finding the sum of the elements of the list
	if sum_of_list > 22: # if sum is greater than 22
		greater_22 += 1
	elif sum_of_list <= 17: # if sum is less than or equal to 17
		less_equal_17 += 1

# printing the values
print("The number of times the sum is greater than 22 is: ", greater_22)
print("The number of times the sum is less than or equal to 17 is: ", less_equal_17)
print("\n")

greater_22 = 0 #variable to keep count of the times the sum is greater than 22
greater_23 = 0 #variable to keep count of the times the sum is greater than 22

#It is part of Q3 
for i in range(100):
	sum_of_list = sum(RollFive()) #calling the function to get the list and finding the sum of the elements of the list
	if sum_of_list > 23: # if sum is greater than 22
		greater_23 += 1
	if sum_of_list > 22: # if sum is less than or equal to 17
		greater_22 += 1

# printing the values
print("The number of times the sum is greater than 22 is: ", greater_22)
print("The number of times the sum is greater than 23 is: ", greater_23)