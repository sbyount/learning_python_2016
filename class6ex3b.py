# import function
from class6ex3a import ip_validator

ip_addr = raw_input("\nPlease enter an IP address to validate: ")

if ip_validator(ip_addr):
    print "\nThat IP address IS valid.\n"

else:
    print "\n That IP address is NOT valid\n"
