import re

f = open('ospf_single_interface.txt')

ospf_dict = {}

for line in f:

    intf = re.search(r'^(.+) is up, line protocol is up', line)
    if intf:
        ospf_dict['Int'] = intf.group(1)

    ip = re.search(r'Internet Address (.+), Area (.+),', line)
    if ip:
        ospf_dict['IP'] = ip.group(1)
        ospf_dict['Area'] = ip.group(2)

    network_type = re.search(r'Network Type (.+),', line)
    if network_type:
        ospf_dict['Type'] = network_type.group(1)

    cost = re.search(r'Cost: (.+)', line)
    if cost:
        ospf_dict['Cost'] = cost.group(1)

    timers = re.search(r'Hello (.+), Dead (.+?),', line)
    if timers:
        ospf_dict['Hello'] = timers.group(1)
        ospf_dict['Dead'] = timers.group(2)

print_order = ('Int', 'IP', 'Area', 'Type', 'Cost', 'Hello', 'Dead')

for k in print_order:
    print "%10s: %-20s" % (k, ospf_dict[k])
print
