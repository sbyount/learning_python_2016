def valid_ip(ip_address):
    '''
    Check if the IP address is valid
    Return either True or False
    '''

    # Make sure IP has four octets
    octets = ip_address.split('.')
    if len(octets) != 4:
        return False

    # convert octet from string to int
    for i, octet in enumerate(octets):
        try:
            octets[i] = int(octet)
        except ValueError:
            # couldn't convert octet to an integer
            return False

    # map variables to elements of octets list
    first_octet, second_octet, third_octet, fourth_octet = octets

    # Check first_octet meets conditions
    if first_octet < 1:
        return False
    elif first_octet > 223:
        return False
    elif first_octet == 127:
        return False

    # Check 169.254.X.X condition
    if first_octet == 169 and second_octet == 254:
        return False

    # Check 2nd - 4th octets
    for octet in (second_octet, third_octet, fourth_octet):
        if (octet < 0) or (octet > 255):
            return False

    # Passed all of the checks
    return True
