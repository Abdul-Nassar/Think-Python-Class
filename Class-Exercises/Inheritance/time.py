import sys

class Time(object):

	def __init__(self, hour = 0, minute = 0, second = 0):
		self.hour = hour
		self.minute = minute
		self.second = second
	
	def __str__(self):
		return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

	def __cmp__(self, other):
		t1 = self.hour, self.minute, self.second
		t2 = other.hour, other.minute, other.second
		return cmp(t1, t2)
def main():
	time = Time()
	print time
	t1 = Time(11, 45, 30)
	t2 = Time(12, 45, 30)
	t = cmp(t1, t2)
	print t
	if t == 0:
		print t1,
		print ' and ',
		print t2,
		print 'are equal'
	elif t > 0:
		print t1,
		print ' is greater than ',
		print t2,
	else:
		print t1,
		print ' is Less than ',
		print t2,
		
if __name__=='__main__':
	main()
	
