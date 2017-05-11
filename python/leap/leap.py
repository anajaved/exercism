#Leap years divisible by 4, except when divisibly by 100, unless divisible by 400.

def is_leap_year(year):
	years = year % 4
	if years != 0:
	    return False
	else:
	    hund = year % 100
	    if hund == 0:  #if divisble by 100
	        if (year%400) == 0: 
	            return True
	        else:
	            return False
	            
	    else:
	        return True 
