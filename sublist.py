def listWithinList(X, Y): #defining the predicate
	Y = Y[1:-1] #removing the first and last element of Y
	if len(X) > len(Y): #checking if the length of X is > length of Y. 
	#A sublist cannot be longer than the list to be checked againt
		return False #if it is longer, we return false
	length = 0 # we take a length variable to check whether the loop executes till the end of list X is encountered
	for (x, y) in zip(X, Y): # the loop loops through both the lists X and Y
	# this loop goes till the length of X because X has the smaller length
		if x == y: # checking the value from list X with value from list Y
			length += 1 #incrementing length to keep track of X
		elif x != y: # if values are not equal, it breaks the loop
			length -= 1
			break

	if length == len(X): # checks if length of X is equal to length
		return True #returns true
	else: # if length != X's length it will return false
		return False

print(listWithinList(['b','c','d'],['a','b','c','d','e'])) # gives output True as [b,c,d] is present in [a,b,c,d,e]
print(listWithinList(['b','c','d','e'],['a','b','c','d','e'])) # gives output False [b,c,d,e] is present in [a,b,c,d,e] but e is last element
print(listWithinList(['c','d','e'],['a','b','c','d','e'])) # gives output False [c,d,e] is present in [a,b,c,d,e] but e is last element

X = ['b'] ;
print(listWithinList(X,['a','b','c','d','e']))

X = ['b', 'c'] ;
print(listWithinList(X,['a','b','c','d','e']))

X = ['b', 'c', 'd'] ;
print(listWithinList(X,['a','b','c','d','e']))

X = ['c'] ;
print(listWithinList(X,['a','b','c','d','e']))

X = ['c', 'd'] ;
print(listWithinList(X,['a','b','c','d','e']))

X = ['d'] ;
print(listWithinList(X,['a','b','c','d','e'])) # gives output False

Y = ['_3668', 'b', 'c', 'd', 'e', '_3674'] 
print(listWithinList(['b','c','d','e'],Y))

Y = ['_3668', 'b', 'c', 'd', 'e', '_3698', '_3674'] 
print(listWithinList(['b','c','d','e'],Y))

Y = ['_3668', '_3680', 'b', 'c', 'd', 'e', '_3674'] 
print(listWithinList(['b','c','d','e'],Y))

Y = ['_3668', 'b', 'c', 'd', 'e', '_3716', '_3698', '_3674'] 
print(listWithinList(['b','c','d','e'],Y))

Y = ['_3668', '_3680', 'b', 'c', 'd', 'e', '_3698', '_3674'] 
print(listWithinList(['b','c','d','e'],Y)) # gives output False


