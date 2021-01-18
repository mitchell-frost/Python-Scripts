def numbers(arr): # this function takes input of 20 numbers from the user
	for i in range(0, 21): # the loop goes from 0 to 20
		x = input("Enter a number: ") # this takes an input from the user
		x = int(x) # it changes the string input to an integer
		arr.append(x) # this adds the value to the list

def  display(arr): # this function displays the array
	for i in range(len(arr)): # this loop iterates over the loop
		print(arr[i], end=" ") # printing the value in the list
		
	print("\n") # creates a newline

def highest_number(arr): # this function finds the highest number of the list
	max = arr[0]  # max is initialised to first value of list
	for i in range(0, 21): # iterates over the list
		if (arr[i] > max): # if list value is greater than max value
			max = arr[i] # list value is initialised to max

	print("The highest number in the list is : ", max) # maximum value is printed

def lowest_number(arr): # this function finds the lowest/smallest number of the list
	min =  arr[0] # min is initialised to first value of list
	for i in range(0, 21): # iterates over the list
		if (arr[i] < min): # if list value is less than min value
			min = arr[i] # list value is initialised to min

	print("The lowest number in the list is : ", min) # minimum value is printed

def total_avg(arr): # this function finds the total and average of the numbers of the list
	total = 0 # total variable is initialized to 0
	avg = 0 # average variable is initialized to 0
	for i in range(0, 21): # iterates over the list
		total = total + arr[i] # value in the list is added to total variable

	avg = total / len(arr) # average is found by dividing the total by size of the list

	print("The total of the numbers: ", total) # total value is printed
	print("The average of the numbers is: ", avg) # average value is printed

def main(): # driver function for all the functions
	A = [] # list is initialised
	numbers(A) # input numbers function is called
	display(A) # list is displayed
	highest_number(A) # maximum value is found out and displayed
	lowest_number(A) # minimum value is found out and displayed
	total_avg(A) # average value is found out and displayed

main() # main function is called