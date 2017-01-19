'''
Classes and objects
'''
class IPAddress(object):

    # initialize ip_addr object
    def __init__(self, ip_addr):
        self.ip_addr = ip_addr

    # function to convert ipv4 to binary.
    def display_in_binary(self):
        '''
        display IP address in dotted decimal notation, padded to eight digits.
        '''

        # split the string into a LIST at the decimal point.
        octets = self.ip_addr.split(".")

        # create a blanklist to append later
        ip_addr_bin = []

        # For each element
        for octet in octets:

            # convert the string to int and then into binary
            # put the binary representation of the integer of that octet into var.
            bin_octet = bin(int(octet))

            # strip off the 'ob' string tag
            bin_octet = bin_octet[2:]

            # prepend zeros to the value to make it total eight digits
            while True:
                if len(bin_octet) >= 8:
                    break
                bin_octet = '0' + bin_octet

            # Add each new element to the new list
            ip_addr_bin.append(bin_octet)

        # join the binary number in binary format
        ip_addr_bin = ".".join(ip_addr_bin)

        return ip_addr_bin

    #function to display ip address to hex
    def display_in_hex(self):
        '''
        display IP address in two digit hex notation
        '''
        # split the string into a LIST at the decimal point.
        octets = self.ip_addr.split(".")

        # create a blanklist to append later
        ip_addr_hex = []

        # For each element
        for octet in octets:

            # convert the string to int and then into binary
            # put the binary representation of the integer of that octet into var.
            hex_octet = hex(int(octet))

            # strip off the 'ob' string tag
            hex_octet = hex_octet[2:]

            # prepend zeros to the value to make it total eight digits
            while True:
                if len(hex_octet) >= 2:
                    break
                hex_octet = '0' + hex_octet

            # Add each new element to the new list
            ip_addr_hex.append(hex_octet)

        # join the binary number in binary format
        ip_addr_hex = ".".join(ip_addr_hex)

        return ip_addr_hex

    def is_valid(self):
        '''
        Check to make sure the IP is valid.
        Return True or False
        '''

        # check to make sure there are four octets
        octets = self.ip_addr.split('.')
        if len(octets) != 4:
            return False

        # check to make sure the values are integers
        for i, octet in enumerate(octets):
                try:
                    octets[i] = int(octet)
                except ValueError:
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

        # Passed all the checks, return True
        return True


if __name__ == '__main__':
    TEST_IP = ['192.168.1.1', '0.255.1.1', '169.254.1.1', '10.10.10.10']

    for ip in TEST_IP:
        print "\nTesting %s" % ip
        test_ip = IPAddress(ip)
        print "IP in binary: %s" % test_ip.display_in_binary()
        print "IP in hex: %s" % test_ip.display_in_hex()
        print "IP is valid: %s" % test_ip.is_valid()
