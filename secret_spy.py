def encoder(dict, msg): # the function to encode the message. It takes two parameters. dict is the dictionary and msg is the message to be encoded
	message = msg.lower() # storing the lowercase form of the message in a variable for easy checking
	for key in dict: # iterating through the dictionary
		key = key.lower() # converting the key of the dictionary to lowercase because the character is already in lowercase and this will be easy for checking
		if key in message: # checking if the key in the dictionary is present in the message string 
			msg = msg.replace(key, dict[key]) # it the key is present in the message string it is replaced with the value of the key in the dictionary

	print(msg) # printing the final message after desoding it.

encoder({"a":"4", "e":"3", "1":"1"}, "Awesomeness is key") # calling encoder() function with the first example given in question

encoder({"!":"?", ".":",", "a":"aaa"}, "Punctuation, is key. Without it, what will we do!") # calling encoder() function with the second example given in question

encoder({"a":"1", "b":"4", "c":"6", "d":"/", ".":"k", "h":">"}, "The lazy brown fox jumped over the fence.") # random example which can be removed