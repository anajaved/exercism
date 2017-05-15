#Leap years divisible by 4, except when divisibly by 100, unless divisible by 400.

def is_leap_year(year):
	'''
	Takes in an a year (integer) and returns either True or False
	depending on whether the year is considered a leap year
	'''
	
	if (year % 4) != 0:
	    return False
	else:
	    if (year % 100)== 0:  #if divisble by 100
	        if (year%400) == 0: 
	            return True
	        else:
	            return False
	    else:
	        return True 
