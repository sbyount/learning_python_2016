# if/then loop for bad input
# if len(octets) == 3:
#    octets.append('0')
#elif len(octets) == 4:
#    octets[3] = '0'

ip_network = raw_input("\n\nEnter a network: ")

# split the network at dots, assign to variable
octets = ip_network.split(".")
print octets
# Take the first three octets only
octets = octets[:3]
# pad the fourth octet with zero
octets.append('0')

# join it back together into new variables
network_number = ".".join(octets)
print "\nYour network number is: %s" % network_number

# get string representations of the first octet for binary and hex
first_octet_bin = bin(int(octets[0]))
first_octet_hex = hex(int(octets[0]))

# print out the columms and variable values
print "\n\n"
print "%20s %20s %20s" % ("NETWORK_NUMBER", "FIRST_OCTET_BINARY", "FIRST_OCTET_HEX")
print "%20s %20s %20s" % (network_number, first_octet_bin, first_octet_hex)
