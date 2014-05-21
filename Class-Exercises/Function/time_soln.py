import sys
import time
def is_after(t1, t2):
	return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

def increment(t1, seconds):
	assert valid_time(t1)
	seconds +=time_to_int(t1)
	return int_to_time(seconds)

def mul_time(t1, factor):
	assert valid_time(t1)
	seconds = time_to_int(t1) * factor
	return int_to_time(seconds)
	
def days_to_birthday(birthday):
	today = datetime.today()
	next_birthday = datetime(today.year, birthday.month, birthday.day)
	if today > next_birthday:
		next_birthday = datetime(today.year+1, birthday.month, birthday.day)
	delta = next_birthday - today
	return delta.days

def double_day(b1, b2):
	assert b1> b2
	delta = b1-b2
	double_day = b1 + delta
	
def datetime_exercises():
	today = datetime.today()
	print today.weekday()
	print today.strftime('%A')

	birthday = datetime(1989, 4, 9)
	print 'Days Until Birthday : ', days_to_birthday(birthday)
	
	b1 = datetime(2006, 12, 26)
	b2 = datetime(2003, 10, 11)
	print 'Double day : ', double_day(b1, b2)
	
def main():
	noon_time = time.time()
	noon_time.hour = 12
	noon_time.minute = 0
	noon_time.second = 0
	print 'Starts at : ', time.print_time(noon_time)
	
	movie_minutes = 109
	run_time = int_to_time(movie_minutes * 60)
	print 'Run time : ', time.print_time(run_time)
	
	end_time = add_times(noon_time, run_time)
	print 'Ends At : ', time.print_time(end_time)
	
	print 'Does it end after it begins ?',
	print is_after(end_time, noon_time)
	
	print 'Home by : ',
	travel_time =600
	home_time = increment(end_time, travel_time)
	time.print_time(home_time)
	
	race_time = time.time()
	race_time.hour = 1
	race_time.minute = 34
	race_time.second = 05

	print 'Half maraton time : ', time.print_time(race_time)
	
	distance = 13.1
	pace = mul_time,(run_time, 1/distance)
	
	print 'time Per Mile : ', time.print_time(pace)

	datetime_exercises()

if __name__=='__main__':
	main()

