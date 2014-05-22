class Time(object):
	def print_time(time):
		print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)
	
def main():
	start = Time()
	start.hour = 9
	start.minute = 45
	start.second = 00
	Time.print_time(start)

if __name__=='__main__':
	main()

