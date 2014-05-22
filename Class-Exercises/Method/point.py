import sys

class Point(object):
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	def print_point(self):
		print '(%g, %g)' %(self.x, self.y)

def main():
	point = Point()
	point.__init__()
	print 'Initial Point : ', 
	point.print_point()
	
	point = Point(5, 8)
	print 'New Point : ',
	point.print_point()

if __name__=='__main__':
	main()
