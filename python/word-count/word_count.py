def word_count(sentence):
	sentence_dict={}
	sentence=sentence.lower()
	sentence=sentence.replace("_", " ")
	for word in sentence.split():
		if word in sentence_dict:
			sentence_dict[word] +=1 
		else:
			sentence_dict[word] =1
	print sentence_dict



word_count('one of each')
word_count('one fish two fish red fish blue fish')
word_count('wait for       it')