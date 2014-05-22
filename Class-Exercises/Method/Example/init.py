class Time:
	def __init__(self, hour=0, minute = 0, second = 0):
		self.hour = hour
		self.minute = minute
		self.second = second
	def print_time(self):
		print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
	
def main():
	"""time = Time()
	time.__init__()
	print 'Initial Time : ', time.print_time()"""
	time1 = Time(7, 43)
	print 'New time : ', time1.print_time()
if __name__=='__main__':
	main()
