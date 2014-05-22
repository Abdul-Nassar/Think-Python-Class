class Point(object):
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def __add__(self, other):
		self.x = self.x + other.x
		self.y = self.y + other.y
		return self

	def __str__(self):
		return '(%g, %g)' % (self.x, self. y)
	
def main():
	
	point = Point()
	point.__init__()
	
	point1 = Point(5, 6)
	point2 = Point(10, 20)
	
	print 'Point1 : ',
	print point1

	print 'Point2 : ',
	print point2
	
	print 'Sum : ',
	print point1 + point2

if __name__=='__main__':
	main()
