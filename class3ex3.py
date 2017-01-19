# import print method
import pprint

# One big list
show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''

# separeate the list into lines at the newline character
sh_ip_lines = show_ip_int_brief.split("\n")

# create a blank list so we can append to it later
show_ip_list = []

# iterate over the list
for line in sh_ip_lines:
    # skip the header row
    if 'Interface' in line:
        continue

    # break the lines into words
    line_split = line.split()

    if len (line_split) == 6:

        #map the variables to fields in the list
        if_name, ip_addr, discard1, discard2, line_status, proto_status = line_split
        # for lines that are up/up, add them to the list
        if (line_status == "up") and (proto_status == "up"):
            show_ip_list.append((if_name, ip_addr, line_status, proto_status))
            # print columns with 15 characters and 10 characters, left justified (-)
            print ("%-15s" "%-15s" "%-10s" "%-10s") % (if_name, ip_addr, line_status, proto_status)

print "\n"

# use print method
pprint.pprint(show_ip_list)
print "\n"
