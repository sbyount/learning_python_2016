import re
#import class7ex1a

cdp_file = 'sw1_cdp.txt'
f = open(cdp_file)
cdp_data = f.read()
f.close()

tmp_dict = {}

# find one or more "any" chars after Device ID, IP addy
tmp_dict['remote_hosts'] = re.findall(r'Device ID: (.+)', cdp_data)
tmp_dict['IPs'] = re.findall(r'IP address: (.+)', cdp_data)
# find one or more "any" chars after platform.  match only 0 or 1 words
tmp_dict['platform'] = re.findall(r'Platform: (.+?),', cdp_data)

print
field_order = ('remote_hosts', 'IPs', 'platform')
for i in field_order:
    print "%15s: %-20s" % (i, tmp_dict[i])

print
