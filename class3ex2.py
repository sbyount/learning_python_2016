# The list
entry1 = "*  1.0.192.0/18   157.130.10.233     0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24     157.130.10.233     0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24    157.130.10.233     0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233     0 701 6762 6762 6762 6762 38040 9737 i"

# Print headers
print "\n%-20s %-50s" % ("ip_prefix", "as_path")

# Iterate through the list
for entry in (entry1, entry2, entry3, entry4): # For each index in the list
    entry_split = entry.split() # split each row into elements
    ip_prefix = entry_split[1] # put the second element into var
    as_path = entry_split[4:-1] # start and 4th element, go to element prior to the end (get rid of i)
    print "%-20s %-50s" % (ip_prefix, as_path) #print it out

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

version = cisco_ios.split(",")
print "\nThe version is: %s"% version[2]
