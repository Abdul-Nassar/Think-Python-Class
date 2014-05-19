import sys

def main():
	prompt = 'Enter the number : '
	n = int(raw_input(prompt))
	f = factorial(n)
	print "Factorial Of '", n, "': ", f

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

if __name__=='__main__':
	main()
