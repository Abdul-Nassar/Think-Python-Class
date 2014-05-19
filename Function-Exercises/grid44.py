"""
Progam to print the following pattern with function :

+----+----+----+
/    /    /    /
/    /    /    /
/    /    /    /
/    /    /    /
+----+----+----+
/    /    /    /
/    /    /    /
/    /    /    /
/    /    /    /
+----+----+----+
/    /    /    /
/    /    /    /
/    /    /    /
/    /    /    /
+----+----+----+

"""

import sys

def grid(p):
	l = '+'
	m = '-'*4
	n = '/'
	o = ' '*4
	for i in range(p):
		if i != 0 and i != 5 and i!=10 and i!=15:
			print n, o, n, o, n, o, n
		else:
			print l, m, l, m, l, m, l
def main():
	grid(16)

if __name__=='__main__':
	main()

