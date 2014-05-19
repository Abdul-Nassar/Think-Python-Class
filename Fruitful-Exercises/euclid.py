import sys

def main():
	prompt = "Enter a & b : "
	a = int(raw_input(prompt))
	b = int(raw_input())
	g = gcd(a,b)
	print "GCD : ",g
def gcd(a, b):
	if b ==	0:
		return a
	else:
		return gcd(b, a%b)	
	"""while b:
		a, b = b, a%b
	return a
	"""


if __name__=='__main__':
	main()
