import sys #import library

if len(sys.argv) == 2: #if the number of args equals 2 (filename is the 1st one)
    ip_addr = sys.argv.pop() #pop off the last one to variable
    print 'The IP address is: %s' % ip_addr
else:
    print "That was an error."
