class Time(object):
	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second
	
	def print_time(self):
		print str(self)
	
	def __str__(self):
		return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

	def time_to_int(self):
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds

	def is_after(self, other):
		return self.time_to_int() > other.time_to_int()

	def __add__(self, other):
		if isinstance(other, Time):
			return self.add_time(other)
		else:
			return self.increment(other)

	def __radd__(self, other):
		return self.__add__(other)

	def add_time(self, other):
		assert self.is_valid() and other.is_valid()
		seconds = self.time_to_int() + other.time_to_int()
		return int_to_time(seconds)

	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)

	def is_valid(self):
		if self.hour < 0 or self.minute < 0 or self.second<0:
			return False
		if self.minute >= 60 or self.second >= 60:
			return False
		return True

def int_to_time(seconds):
	minutes, second = divmod(seconds, 60)
	hour, minute = divmod(minutes, 60)
	time = Time(hour, minute, second)
	return time

def main():
	time = Time()
	time.__init__()
	
	start = Time(9, 45, 00)
	print "Start Time : ",
	start.print_time()
		
	end = start.increment(1337)
	print "End Time : ",
	end.print_time()

	print 'Is end after start ?',
	print end.is_after(start)

	print 'Using __str__ : '
	print "Start Time : ",
	print start
	print "End Time",
	print end
	
	print "Start Time : ",
	start.print_time()

	duration = Time(1, 35)
	print 'Duration : ',
	duration.print_time()
	
	print 'Correpnding End Time',
	print start + duration

	print 'Start Time : ',
	print start
	print 'Duration : 1337'
	print 'Correpnding End Time',
	print start + 1337

	print 'Start Time : ',
	print start
	print 'Duration : 1337'
	print 'Corresponding End Time : ',
	print 1337 + start
	
	
	print 'Example of polymorphism'
	t1 = Time(7, 43)
	print 'T1 : ',
	print t1
	
	t2 = Time(7, 41)
	print 'T2 : ',
	##t2.print_time()
	print t2
	t3 = Time(7, 37)
	print 'T3 : ',
	##t3.print_time()
	print t3
	
	print 'Total Time : ',
	total = sum([t1, t2, t3])
	print total
	
if __name__=='__main__':
	main()
			
