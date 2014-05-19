import sys

def main():
	prompt = 'Enter values for a,b,c,n : \n'
	a = int(raw_input(prompt))
	b = int(raw_input())
	c = int(raw_input())
	n = int(raw_input())
	if n>2:
		check_fermat(a, b, c, n)
	else:
		print "No, that doesn't work."

def check_fermat(a, b, c, n):
	p = a**n	
	print 'P: ',p
	q = b**n
	print 'Q: ',q	
	r = c**n
	print 'R: ',r
	if p+q == r:
		print "Holy smokes, Fermat was wrong!"
	else:
		print "No, that doesn't work."

"""def power(k,n):
	x = 1
	for i in range(n):
		x = x * k
	return x
"""
if __name__=='__main__':
	main()
