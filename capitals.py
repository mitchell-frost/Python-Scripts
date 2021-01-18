# importing the module 
import random
import ast 

# reading the data from the file called states.txt
with open('states.txt') as f: 
    data = f.read() 
      
# reconstructing the data as a dictionary 
states = ast.literal_eval(data) 
  
ans = "" #initializing answer variable
correct = 0 #initializing variable that keeps track of correct answers
ques_count = 0 #count variable will keep track of the number of questions
questions = []
random_state = ""

while (ans != "0"):
	ques_count += 1 #increments the number of questions

	while True:
		random_state = random.choice(list(states.keys()))
		if questions.count(random_state) > 0:
			continue
		else:
			break

		 #generate random state from the list
	
	questions.append(random_state)  #storing state so that it isn't repeated
	random_capital = states[random_state] #get capital of the random state generated
	random_capital = random_capital.lower() #converts to lowercase
	random_capital = random_capital.replace(" ", "") #removes whitespace for proper checking
	print("What is the capital city of", random_state, "? (enter 0 to quit)") #asks the capital of the random state generated
	ans = input()
	ans = ans.lower() #converts to lower case so that the checking is not case sensitive
	if ans == random_capital: #checking if ans is equal to the random state's capital
		print("That is correct") #prints this if it is correct
		correct += 1 #increments the correct variable to keep track of the number of questions answered correctly
	elif ans != "0":
		print("That is incorrect") #prints this if incorrect

print("You answered", correct, "out of", ques_count, "questions correctly") #prints the total questions answered correctly