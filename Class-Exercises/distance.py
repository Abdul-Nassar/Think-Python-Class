import sys
import math
def main():
	p = point()
	prompt = 'Enter the first point (Two coordinates) : '
	a = int(raw_input(prompt))
	b = int(raw_input())	
	
	prompt = 'Enter the second point (Two coordinates) : '
	c = int(raw_input(prompt))
	d = int(raw_input())

	print 'First ponit : ',
	p.print_point(a, b)
	
	print 'Second ponit : ',
	p.print_point(c, d)
	d = p.distance(a, b, c, d)
	print 'Distance : ', d

class point(object):
	def distance(self, a, b, c, d):
		self.x = (c - a)**2
		self.y = (d - b)**2
		self.d = math.sqrt(self.x + self.y)
		return self.d	
		
	def print_point(self, a, b):
		print '(%g, %g)' % (a, b)

if __name__=='__main__':
	main()
