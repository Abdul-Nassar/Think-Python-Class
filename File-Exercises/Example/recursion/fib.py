import sys

def main():
	prompt = 'Enter the number : '
	n = int(raw_input(prompt))
	f = fibonacci(n)
	print "Fibonacci of '", n, "': ", f	

def fibonacci (n):
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__=='__main__':
	main()
