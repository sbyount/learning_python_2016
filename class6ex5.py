import class6ex3
import class6ex4

ip_address = raw_input('\nPlease enter an IP address: ')

# If the IP address is valid:
if class6ex3.valid_ip(ip_address):

    # Convert the decimal to binary
    ip_addr_bin = class6ex4.ip_converter(ip_address)
    print "\nThe binary output is: %s\n" % ip_addr_bin

else:
    print "\n\tSorry, that IP address is not valid.\n"
