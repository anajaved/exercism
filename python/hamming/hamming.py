# hamming difference:
# measure the minimum number of point mutations that could have occurred on the
# evolutionary path between the two strands.

def distance(strand1, strand2):
    if len(strand1) != len(strand2):
    	raise ValueError ()
    else:
    	count = 0
    	for i, val in enumerate(strand1):
    		if val != strand2[i]:
    			count +=1

    	return count 
    	





