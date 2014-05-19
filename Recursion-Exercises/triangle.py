import sys

def main():
	prompt = "Enter Side of a triangle : \n"
	a = int(raw_input(prompt))
	b = int(raw_input())
	c = int(raw_input())
	y = is_triangle(a, b, c)
	print 'Whether the sides form a Triangle? : ', y
	
def is_triangle(a, b, c):
	if a > b+c or b > a+c or c > a+b:
		return 'No....'
	else:
		return 'Yes....'

if __name__=='__main__':
	main()

