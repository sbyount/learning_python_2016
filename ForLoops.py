a = range(10) # with integers

for i in a: # for each index in the range
  print i

b = 'whatever' # with strings

for i in b:
    print i

i = 0 # set index at 0
for element in a: #add new variable
    a[i] = element**2 # for each list entry, square it
    i += 1 #increment by one.  same and i = i + 1
print a

for test in enumerate(a): # new variable
    print test # prints tuple pairs, index followed by value.

for i, element in enumerate(a): # for each variable in the tuple
    a[i] = element**2 #for each index, square the element
print a
