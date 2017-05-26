#"AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"
#Run length Encoding exercise 


def decode(short_string):
    pass


def encode(long_string):
	'''
	Input: a string of multiple characters (A-Z)
	Output: returns a string, providing one count and one data value for each consecutive characters
	'''

    ongoing_string = ""
    count=0

    for i, val in enumerate(long_string):
    	try:
    		int(val)
    		return long_string
    		break

    	except:
	    	if i != 0:
		    	if val == long_string[i-1]:
		    		count +=1

		    		if i == (len(long_string) -1):
		    			if count == 1:
		    				ongoing_string= ongoing_string + long_string[i-1]
		    			else:
		    				ongoing_string= ongoing_string + str(count) + long_string[i-1]

		    	elif val != long_string[i-1]:
		    		if i == (len(long_string) -1):
		    			if count == 1:
		    				ongoing_string= ongoing_string + long_string[i-1] + long_string[i]
		    			else:
		    				ongoing_string= ongoing_string + str(count) + long_string[i-1] + long_string[i]
		    		else:
		    			if count == 1:
		    				ongoing_string= ongoing_string + long_string[i-1]
		    			else:
		    				ongoing_string= ongoing_string + str(count) + long_string[i-1]
		    			count = 1
	    	else:
		    	count +=1


    return ongoing_string


encode('AABBBCCCC') #'2A3B4C'
encode('XYZ') #XYZ
encode('12WB12W3B24WB') #12WB12W3B24WB 
encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB') #12WB12W3B24WB 

#decode('2 hs2q q2w2 ') #'  hsqq qww  ')