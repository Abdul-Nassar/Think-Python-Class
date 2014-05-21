
class Point(object):
	"""Represents a Point"""
	pass

def print_point(p):
	print '(%g, %g)' % (p.x, p.y)


class Rectangle(object):
	"""Represents a Rectangle"""
	pass

def find_center(rect):
	p = Point()
	p.x = rect.corner.x + rect.width/2.0
	p.y = rect.corner.y + rect.height/2.0
	return p


def grow_rectangle(rect, dwidth, dheight):
	rect.width += dwidth
	rect.height += dheight


def main():
	blank = Point()
	blank.x = 3
	blank.y = 4
	print 'blank',
	print_point(blank)

	box = Rectangle()
	box.width = 100.0
	box.height = 200.0
	box.corner = Point()
	box.corner.x = 0.0
	box.corner.y = 0.0

	center = find_center(box)
	print 'center',
	print_point(center)

	print 'Old width : ', box.width
	print 'Old height : ', box.height
	prompt = 'Enter Values for (dx, dy) : '
	a = int(raw_input(prompt))
	b = int(raw_input())
	print '\nGrow\n'	
	grow_rectangle(box, a, b)
	print 'New width : ', box.width
	print 'New height : ', box.height


if __name__ == '__main__':
    main()


