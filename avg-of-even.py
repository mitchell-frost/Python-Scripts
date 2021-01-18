def avg(arr): # the function that finds the average of the even indices elements
	total = 0 # this variable finds the total of the elements at even indices only
	divisor = 0 # this variable counts the number of even indices
	for i in range(len(arr)): # a loop that goes from 0 to the length of the array
		if i % 2 == 0: # checks if the index is even or not
			total += arr[i] # if the index is even, the value at that index is added to the total variable
			divisor += 1 # the divisor is incremented by 1

	average = total / divisor # the average is found by dividing the total by the divisor found out
	return average # average is returned back

def main(): # main function to call above function
	A = [] # a list or array is declared
	A.append(12) # element added to list A
	A.append(45) # element added to list A
	A.append(4) # element added to list A
	A.append(-98) # element added to list A
	val = avg(A) # average function is called to give the avg at the even indices only
	print(val) # value which is the avg is printed. In this case it is, A[0] + A[2] / 2 = (12 + 4) / 2 = 8.0

main() # calling the main function