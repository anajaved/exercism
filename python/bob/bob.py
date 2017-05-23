def hey(statement):
    statement = statement.replace(" ", "")

    if statement.endswith("?"):
    	statement= statement.strip("?")
    	if statement.upper() == statement:
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

    elif len(statement) == 0:
    	return "Fine. Be that way!"

    else:
    	return "Whatever."



hey("Let's go make out behind the gym!") #Whatever.

hey("WATCH OUT!") #chill out

hey("1, 2, 3") #whatever.

hey("4?") #sure`

hey("") #"Fine. Be that way!"



