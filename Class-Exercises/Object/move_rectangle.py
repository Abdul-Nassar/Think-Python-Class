import sys
import copy
import math
import rectangle
def distance_bw_points(p1, p2):
	dx = p1.x - p2.x
	dy = p1.y - p2.y
	dist = math.sqrt(dx**2 + dy**2)
	return dist

def move_rect(rect, dx, dy):
	rect.corner.x +=dx
	rect.corner.y +=dy
	
def move_rect_copy(rect, dx, dy):
	new = copy.deepcopy(rect)
	move_rect(new, dx, dy)
	return new

def main():
	blank = rectangle.Point()
	blank.x = 0
	blank.y = 0
	
	grosse = rectangle.Point()
	grosse.x = 3
	grosse.y = 4
	print 'Point1 : ', rectangle.print_point(blank)
	print 'Point2 : ', rectangle.print_point(grosse)
	print '\n Distance between two points : ',
	print distance_bw_points(grosse, blank)
	
	box = rectangle.Rectangle()
	box.width = 100.0
	box.height = 200.0
	box.corner = rectangle.Point()
	box.corner.x = 50.0
	box.corner.y = 50.0
	
	print box.corner.x
	print box.corner.y
	print 'Move : '
	move_rect(box, 50, 100)
	print box.corner.x
	print box.corner.y
	
	new_box = move_rect_copy(box, 50, 100)
	print 'New Box : ',
	print new_box.corner.x
	print new_box.corner.y
	
if __name__=='__main__':
	main()
