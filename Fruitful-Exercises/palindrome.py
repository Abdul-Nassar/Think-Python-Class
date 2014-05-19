import sys

def main():
	prompt = "\nEnter The String : "
	s = raw_input(prompt)
	a = is_pal(s)
	if a:
		print '\n\tPalindrome\n'
	else:
		print '\n\tNot Palindrome\n'

def is_pal(string):
	if len(string) <=1:
		return True
	if first(string) != last(string):
		return False
	return is_pal(mid(string))

def first(string):
	return string[0]

def last(string):
	return string[-1]

def mid(string):
	return string[1:-1]

if __name__=='__main__':
	main()

