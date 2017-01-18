import sys

#filename, ip_addr = argv
if len(sys.argv) != 2:
    # Exit the script
    sys.exit("Usage: ./ex4_ip_address_valid.py <ip_address>")

ip_addr = sys.argv.pop()

# use a bool to represent validity of the ip address
valid_ip = True

octets = ip_addr.split('.')
if len(octets) != 4:
    sys.exit("\n\nInvalid IP address: %s\n" % ip_addr)

# convert from string to int.
for i, octet in enumerate(octets):
    try:
        octets[i] = int(octet)
    except ValueError:
        # could not convert to string
        sys.exit("\n\nInvalid IP address: %s\n" % ip_addr)

# map variables to elements of the octets list
(first_octet, second_octet, third_octet, fourth_octet) = octets

# check the first octet
if first_octet < 1:
    valid_ip = False
elif first_octet > 223:
    valid_ip = False
elif first_octet == 127:
    valid_ip = False

#check 169.254.x.x condition
if first_octet == 169 and second_octet == 254:
    valid_ip = False

for octet in (second_octet, third_octet, fourth_octet):
    if (octet < 0) or (octet > 255):
        valid_ip = False

if valid_ip == True:
    print ("\n\nGood IP: %s\n") % ip_addr
else:
    sys.exit("\n\nInvalid IP address: %s\n" % ip_addr)
