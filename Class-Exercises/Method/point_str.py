import sys

class Point(object):
	
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def __str__(self):
		return '(%g, %g)' % (self.x, self.y)

	def print_point(self):
		print str(self)

def main():
	point = Point()
	point.__init__()

	print 'Inital : ',
	point.print_point()
	
	print 'New : ',
	point = Point(5, 10)
	point.print_point()
	
if __name__=='__main__':
	main()
