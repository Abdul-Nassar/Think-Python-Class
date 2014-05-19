import sys

def do_four(print_spam,k):
	for i in range(4):
		print_spam(k)		
def print_spam(k):
	print k

def main():
	l='spam'
	do_four(print_spam, l)
	i=0
if __name__=='__main__':
	main()
