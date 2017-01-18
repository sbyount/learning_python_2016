# IP converter Function

# Function pads each octet with leading zeros
def binary_pad(bin_octet):
    while True:
        if len(bin_octet) >= 8:
            break
        bin_octet = '0' + bin_octet
    return bin_octet

# Function that converts IPV4 decimal to Binary
def ip_converter(ip_addr):

    octets = ip_addr.split(".")

    # create a blank list (needed because I use .append() method below)
    ip_addr_bin = []

    if len(octets) == 4:

        for octet in octets:
            # convert the integer version of the string to Binary
            bin_octet = bin(int(octet))

            # strip off '0b' from front of string (you can slice a string also)
            bin_octet = bin_octet[2:]

            #call the padding function on each octet
            bin_octet = binary_pad(bin_octet)

            # prepend '0' to number until 8 chars long
            #while True:
            #    if len(bin_octet) >= 8:
            #        break
            #    bin_octet = '0' + bin_octet

            # add octet to new list
            ip_addr_bin.append(bin_octet)

        # join binary number in dotted-binary format
        ip_addr_bin = ".".join(ip_addr_bin)

        return ip_addr_bin

    else:
        return("Invalid IP address entered")
