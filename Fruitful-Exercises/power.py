import sys

def main():
	prompt = "Enter Two Numbers : "
	a = int(raw_input(prompt))
	b = int(raw_input())
	p = is_power(a, b)
	if p:
		print "\n", a, " is a power of ",b
	else:
		print "\n", a, " is not a power of ",b

def is_power(a, b):
	if a % b ==0 and is_power(a/b,b) ==0 and a>b:
		return True
	return False
	
if __name__=='__main__':
	main()

