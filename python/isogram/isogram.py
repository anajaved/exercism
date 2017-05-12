def is_isogram(word):
    if type(word) == str:
    	unique_char = list()
    	char_count = list()
    	word = word.lower()
    	word = word.replace(" ", "")
    	word = word.replace("-", "")
    	word = word.replace("_", "")
    	for each in set(word):
    		unique_char.append(each)
    	for each in word:
    		char_count.append(each)

    	if len(unique_char) == len(char_count):
    		return True
    	else: 
    		return False

 
