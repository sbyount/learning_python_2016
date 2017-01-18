'''
IP address with netmask
'''

from class9ex1 import IPAddress

class IPAddressWithNetmask(IPAddress):
    '''
    Add a netmask to the IP address class
    '''

    def __init__(self, ip_addr):
        (ip_addr, netmask) = ip_addr.split('/')
        self.netmask = '/' + netmask

        # Call the base class
        IPAddress.__init__(self, ip_addr)

    def netmask_in_dotdecimal(self):
        '''
        Display the netmask in dotted decimal notation
        '''
        # Use the fact that you can repeat a string via multiplication
        netmask = int(self.netmask.strip('/'))
        one_string = '1' * netmask

        #Number of zeros
        zero_string = '0' * (32 - netmask)

        # New netmask string
        netmask_str = one_string + zero_string

        # Get each octet
        octet1 = netmask_str[:8]
        octet2 = netmask_str[8:16]
        octet3 = netmask_str[16:24]
        octet4 = netmask_str[24:32]
        netmask_tmp = [octet1, octet2, octet3, octet4]

        # convert from binary to decimal
        for i, octet in enumerate(netmask_tmp):
            # It must be a string to use the join method
            netmask_tmp[i] = str(int(octet, 2))

        return '.'.join(netmask_tmp)

def main():
    test_ip2 = IPAddressWithNetmask('172.31.255.1/24')

    print
    print "%15s: %40s" % ('IP', test_ip2.ip_addr)
    print "%15s: %40s" % ('Netmask', test_ip2.netmask)
    print "%15s: %40s" % ('Binary IP', test_ip2.display_in_binary())
    print "%15s: %40s" % ('Hex IP', test_ip2.display_in_hex())
    print "%15s: %40s" % ('IP Valid', test_ip2.is_valid())
    print "%15s: %40s" % ('Netmask dot dec', test_ip2.netmask_in_dotdecimal())
    print


if __name__ == '__main__':
    main()
