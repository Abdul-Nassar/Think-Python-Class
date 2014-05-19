import sys

def main():
	prompt = 'Enter values for m & n : '
	m = int(raw_input(prompt))
	n = int(raw_input())
	a = ackermann(m, n)
	print "ack(", m, ", ", n, ") : ", a
#computes ackermann function A(m, n)	
def ackermann(m, n):
	if m==0:
		return n+1
	if n==0:
		return ackermann(m-1,1)
	return ackermann(m-1, ackermann(m,n-1))

if __name__=='__main__':
	main()
