# Get the ip address
ip_address = raw_input("Please enter in IPV4 address: ")
# Split input into a list
octets = ip_address.split(".")
# Get binary value from each element and put into variables
first_octet_bin = bin(int(octets[0]))
seccond_octet_bin = bin(int(octets[1]))
third_octet_bin = bin(int(octets[2]))
fourth_octet_bin = bin(int(octets[3]))

print "\n"
# Print columms
print "%s %20s %20s %20s" % ("FIRST", "SECOND", "THIRD", "FOURTH")
# print list
print "%s %20s %20s %20s" % (first_octet_bin, seccond_octet_bin, third_octet_bin, fourth_octet_bin)

# Join binary back together
binary_address = first_octet_bin + seccond_octet_bin + third_octet_bin + fourth_octet_bin
digits = len(binary_address)

# print results
print "\n"
print ("The binary number is: %s %5s") % (binary_address, digits)
