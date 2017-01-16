a = range(10)
b = range(20)

for i in a:
    print i # print value at index i
    if i == 6:
        continue # skip to the end on this loop
    print 'hello world'

for i in a:
    print i
    if i == 6:
        break # exit the loop altogether
    print 'hello world'

for i in a:
    for j in b:
        if j == 5:
            print "j is 5!"
            break # breaks ouf of the inner loops
        print 'Hello World'

for i in a:
    pass #placeholder for do nothing - no op
