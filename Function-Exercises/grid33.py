"""
Progam to print the following pattern with function :

+----+----+
/    /    /
/    /    /
/    /    /
/    /    /
+----+----+
/    /    /
/    /    /
/    /    /
/    /    /
+----+----+

"""


import sys

def grid():
	l='+'
	m='-'
	n='/'
	o=' '
	for i in range(11):
		if i!=0 and i!=5 and i!=10:
			print n, o*4, n, o*4, n
		else:
			print l, m*4, l, m*4, l

def main():
	grid()



if __name__=='__main__':
	main()
