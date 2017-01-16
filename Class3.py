a = 10
b = 20
c = 30

#if expression: # If true, do these things, then skip tp end
  #statement
  #statement
#elif expression: # If above false but this true, do these things, skip to end
  #statement
  #statement
#else: # If none of the above true, do this.  skip to end
  #statement
  #statement

#Outside of conditional

if a == 10:
    print "a is 10"
    if b == 20:
        print "b is 20"
else:
    print 'something else'

if (a == 10) and (b == 20) and (c == 30):
    print "All are true."
