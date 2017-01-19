# Function to valide an ip address according to specific rules

debug = False

def ip_validator(ip_addr):
    '''Validates an IP argument and returns True or False'''

    # Continue the loop until this is False
    not_done = True

    # Get the IP address.  Continue looping until IP address is valid or CNTRL C.
    while not_done:
        #ip_addr = raw_input("\nPlease enter an IP address to validate: ")

        valid_ip = True

        # split the ip address into a list, separated by "."
        octets = ip_addr.split('.')
        if len(octets) != 4:
            # sys.exit("\nInvalid IP address: %s. 4 octets are required, delimited by '.'.\n " % ip_addr)
            #print "\nInvalid IP address: %s. 4 octets are required, delimited by '.'.\n " % ip_addr
            #continue
            return False

        # convert from string to int.
        for i, octet in enumerate(octets):
                try:
                    octets[i] = int(octet)
                except ValueError:
                    # could not convert to int
                    #-print "\nInvalid IP address: %s. Only integers are allowed.\n" % ip_addr
                    valid_ip = False
                    # sys.exit("\nInvalid IP address: %s. Only integers are allowed.\n" % ip_addr)

        # go to the next iteration of the loop if all 4 are not integers
        if not valid_ip:
            #-print "\nOne or more octets is not an integer or is blank", \
            #    "Please try again."
            valid_ip = False
        # map variables to elements of octets list
        first_octet, second_octet, third_octet, fourth_octet = octets

        # Check first_octet meets conditions
        if first_octet < 1:
            valid_ip = False
        elif first_octet > 223:
            valid_ip = False
        elif first_octet == 127:
            valid_ip = False

        # Check 169.254.X.X condition
        if first_octet == 169 and second_octet == 254:
            valid_ip = False

        # Check 2nd - 4th octets
        for octet in (second_octet, third_octet, fourth_octet):
            if (octet < 0) or (octet > 255):
                valid_ip = False

        # If none of the above match, the IP is good.
        if valid_ip:
            not_done = False
            return valid_ip
        # Otherwise it is bad.  Print the error and start the loop again.
        else:
            return False
            #print "\nSomething is wrong, please try again."

# If the loop exits, the IP is valid.  Print confirmation message.
# print "\nYour IP address %s is valid.\n" % ip_addr

if debug:
    print ip_validator('128.168.1.1')

if __name__ == '__main__':

    ip_address_list = [
    '192.168.1',
    '10.1.1.',
    '10.1.1.x',
    '0.77.22.19',
    '-1.88.99.17',
    '241.17.17.9',
    '127.0.0.1',
    '169.254.1.9',
    '192.256.7.7',
    '192.168.-1.7',
    '10.1.1.256',
    '1.1.1.1',
    '223.255.255.255',
    '223.0.0.0',
    '10.200.255.1',
    '192.168.17.1'
    ]

    # dictionary
    test_ip_addresses = {}

    for item in ip_address_list:
        test_ip_addresses = item, ip_validator(item)
        print test_ip_addresses
