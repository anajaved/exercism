import collections

def word_count(sentence):
	'''
	function takes in a sentence, and returns a dictionary
	of each word's count. Takes in account words with 
	unnecessary punctuations & removes them. 
	'''

	sentence_dict={}
	sentence=sentence.lower()
	punctuation = ["_", ".",",","!","&","@","%","^", "$", ":"]
	for each in punctuation:
		sentence=sentence.replace(each, " ")

	for word in sentence.split():
		if word in sentence_dict:
			sentence_dict[word] +=1 
		else:
			sentence_dict[word] =1
	return sentence_dict 



word_count('car : carpet as java : javascript!!&@$%^&')
word_count('hey,my_spacebar_is_broken.')