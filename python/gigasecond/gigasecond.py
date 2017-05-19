from datetime import datetime, timedelta

def add_gigasecond(birthday):
    '''
	Calculate the moment when someone has lived for 10^9 seconds.
	Input: birthday
	Output: date when a person has lived for 10^9 seconds (gigasecond)
    '''

    birthday += timedelta(seconds=1000000000)
    return birthday

add_gigasecond(datetime(2011, 4, 25))
add_gigasecond(datetime(1977, 6, 13))
