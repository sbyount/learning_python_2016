# Get an IP address from user and validate.

# Continue the loop until this is False
not_done = True

# Get the IP address.  Continue looping until IP address is valid or CNTRL C.
while not_done:
    ip_addr = raw_input("\nPlease enter an IP address to validate: ")

    valid_ip = True

    # split the ip address into a list, separated by "."
    octets = ip_addr.split('.')
    if len(octets) != 4:
        # sys.exit("\nInvalid IP address: %s. 4 octets are required, delimited by '.'.\n " % ip_addr)
        print "\nInvalid IP address: %s. 4 octets are required, delimited by '.'.\n " % ip_addr
        continue

    # convert from string to int.
    for i, octet in enumerate(octets):
        try:
            octets[i] = int(octet)
        except ValueError:
            # could not convert to int
            print "\nInvalid IP address: %s. Only integers are allowed.\n" % ip_addr
            valid_ip = False
            # sys.exit("\nInvalid IP address: %s. Only integers are allowed.\n" % ip_addr)

    # go to the next iteration of the loop if all 4 are not integers
    if not valid_ip:
        print "\nOne or more octets is not an integer or is blank", \
            "Please try again."

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
    # Otherwise it is bad.  Print the error and start the loop again.
    else:
        print "\nSomething is wrong, please try again."

# If the loop exits, the IP is valid.  Print confirmation message.
print "\nYour IP address %s is valid.\n" % ip_addr
