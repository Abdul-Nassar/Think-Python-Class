import sys
import os

def main():
	##name = sys.argv[1]
	##print name
	p = 'are'
	r = 'was'
	s = sys.argv[1]
	print s
	d = sys.argv[2]
	print d
	sed(p, r, s, d)

def sed(p, r, s, d):
	##try:
	fin = open(s,'r')
	fout = open(d, 'w')
	for line in fin:
		line = line.replace(p, r)
		fout.write(line)
	fin.close()
	fout.close()
	##except:
	##	print 'Something Went Wrong'
	
if __name__=='__main__':
	main()
