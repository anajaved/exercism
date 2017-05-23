def hey(statement):
	'''
	Input: string
	Output: returns appropriate response in string format

	Function Bob answers 'Sure.' if you ask him a question.
	He answers 'Whoa, chill out!' if you yell at him.
	He says 'Fine. Be that way!' if you address him without actually saying anything.
	He answers 'Whatever.' to anything else.
	'''


	punct = [" ", ",", "-", "\'", ":", ")", "("]
	for each in punct:
		statement = statement.replace(each, "")

	if statement.endswith("?"):
		statement= statement.strip("?")
		if (statement.upper() == statement) & (len(statement)>0):
			try:
				int(statement) == True
				return "Sure."
			except:
				return "Whoa, chill out!"
		else:
			return "Sure."

	elif statement.endswith("!"):
		if (statement.upper() == statement):
			return "Whoa, chill out!"
		else:
			return "Whatever."

	elif (len(statement) == 0) | ("\t" in statement):
		return "Fine. Be that way!"

	elif statement.upper() == statement:
		try:
			int(statement)
			return "Whatever."
		except:
			return "Whoa, chill out!"

	else:
		return "Whatever."



hey("Let's go make out behind the gym!") #Whatever.
hey("WATCH OUT!") #Whoa, chill out!
hey("1, 2, 3") #Whatever.
hey("4?") #Sure
hey("") #"Fine. Be that way!"

