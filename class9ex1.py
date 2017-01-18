class IPAddress(object):
    '''
    A class representing an IP address
    '''

    def __init__(self, ip_addr):
        self.ip_addr = ip_addr


    def display_in_binary(self):
        '''
        Display the IP address in dotted binary format padded to eight
        digits:
        11000000.10101000.00000001.00000001
        '''

        octets = self.ip_addr.split(".")

        binary_ip = []
        for octet in octets:
            # convert octet to binary
            octet_bin = bin(int(octet))
            octet_bin = octet_bin.split('0b')[1]

            # pad to 8 digits using rjust() method
            octet_bin = octet_bin.rjust(8, '0')
            binary_ip.append(octet_bin)

        return ".".join(binary_ip)


    def display_in_hex(self):
        '''
        Display the IP address in dotted hex format padded to eight
        digits:
        c0.a8.01.01
        '''

        octets = self.ip_addr.split(".")

        hex_ip = []
        for octet in octets:
            # convert octet to hex
            octet_hex = hex(int(octet))
            octet_hex = octet_hex.split('0x')[1]

            # pad to 2 digits using rjust() method
            octet_hex = octet_hex.rjust(2, '0')
            hex_ip.append(octet_hex)

        return ".".join(hex_ip)


    def is_valid(self):
        '''
        Check if the IP address is valid
        Return either True or False
        '''

        # Make sure IP has four octets
        octets = self.ip_addr.split('.')
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




if __name__ == "__main__":

    # Some simple testing
    TEST_IP = ['192.168.1.1', '0.255.1.1']

    for ip in TEST_IP:
        print "\nTesting IP: %s" % ip
        test_ip = IPAddress(ip)
        print "IP in binary: %s" % test_ip.display_in_binary()
        print "IP in hex: %s" % test_ip.display_in_hex()
        print "IP is valid: %s" % test_ip.is_valid()
        print
