def is_pangram(word):
    if type(word) == str:
    	unique_char = list()
    	word = word.lower()
    	word = word.strip('"')

    	punctuation = [" ", ".", "-", "_"]
    	for each in punctuation:
			word = word.replace(each, "")
    	
    	for each in set(word):
    		try: 
    			int(each)
    			continue  #skip over numbers 
    		except:
    			unique_char.append(each)

    	if len(unique_char) != 26:
    		return False
    	else: 
    		return True
