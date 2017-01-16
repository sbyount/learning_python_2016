# This is a decimal to binary converter from Learning Python Week 3.
# Enter filename plus IP address at command line.
import sys

# if there are no args or extra args, exit.
if len(sys.argv) != 2:
    # exit
    sys.exit("Usage: filename + ip address")

# pop off the second element into the var
ip_addr = sys.argv.pop()
# split the string into a LIST at the decimal points.
octets = ip_addr.split(".")

# create a blanklist to append later
ip_addr_bin = []

# If there are four octets (GOOD!)
if len(octets) == 4:

    # For each element
    for octet in octets:

        # first check to make sure octets are valid ip's
        if int(octet) > 255:
            sys.exit("\n0 to 255 are valid octets.")

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
    ip_addr_bin = " ".join(ip_addr_bin)

    # print the output
    print "\n%-15s %-45s" % ("IP Address", "Binary")
    print "%-15s %-45s" % (ip_addr, ip_addr_bin)

else: # if there is anything other than four octets
    sys.exit("Invalid IP address entered.")
