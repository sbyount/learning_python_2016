import pprint

show_version = '''
>>>>> show version data <<<<<
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support:
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X

License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices

Configuration register is 0x2102
>>>>> end <<<<<
'''

# convert tht show_version to a list, one entry per linne
show_version_list = show_version.split('\n')

# initialize the dictionary
router_dict = {}

# Iterate over the sh version data
for line in show_version_list:

    # get vendor and os version
    if 'Cisco IOS Software' in line:
        router_dict['vendor'] = 'Cisco'
        os_version = line.split(',')[2] # get the thrid element in the line
        router_dict['os_version'] = os_version.split('Version ')[1] # second word in element?

    # get model
    if 'bytes of memory' in line:
        router_dict['model'] = line.split()[1] # the second word in the line is the model

    # get serial number
    if 'Processor board ID' in line:
        router_dict['serial_number'] = line.split('Processor board ID ')[1]

    # get uptime
    if ' uptime is ' in line:
        uptime = line.split(' uptime is ')[1]
        uptime = uptime.strip()
        router_dict['uptime'] = uptime

# print dict to std output
print
pprint.pprint(router_dict)
print
