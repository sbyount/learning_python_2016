# imports
import pprint

# read in the variables from the cdp data file
from cdp_data import (sw1_show_cdp_neighbors_detail,
r1_show_cdp_neighbors_detail,
r2_show_cdp_neighbors_detail,
r3_show_cdp_neighbors_detail,
r4_show_cdp_neighbors_detail,
r5_show_cdp_neighbors_detail)

# put cdp data in a list
cdp_neighbors = (
    sw1_show_cdp_neighbors_detail,
    r1_show_cdp_neighbors_detail,
    r2_show_cdp_neighbors_detail,
    r3_show_cdp_neighbors_detail,
    r4_show_cdp_neighbors_detail,
    r5_show_cdp_neighbors_detail,
)

# initialize dictionary
network_devices = {}

# for each device data set
for cdp_data in cdp_neighbors:

    # split the data set into lines
    cdp_data_line = cdp_data.split('\n')

    # set router_name to null for each loop
    hostname = ''

    # for each line in a device blob
    for line in cdp_data_line:

        # set hostname to '' at header
        if '-------------------------' in line:
            hostname = ''

        # get the router_name if it is in the line
        if 'Device ID: ' in line:
            (junk, hostname) = line.split('Device ID: ')
            hostname = hostname.strip()

            # the first time through, initialize the inner dictionary
            if not hostname in network_devices:
                network_devices[hostname] = {}

        # get ip address if it is in the line
        if 'IP address: ' in line:
            (junk, ip) = line.split('IP address: ')
            ip = ip.strip()

            if hostname:
                network_devices[hostname]['ip'] = ip

        # get vendor, model and device_type
        if 'Platform: ' in line:

            # split the platform and copabilities segments
            (platform, capabilities) = line.split(',')

            # get vendor and model from first segments
            (junk, model_vendor) = platform.split('Platform: ')
            (vendor, model) = model_vendor.split()

            # get model and capabilities from second segment
            (junk, capabilities) = capabilities.split('Capabilities: ')
            if 'Router' in capabilities:
                device_type = 'router'
            elif 'Switch' in capabilities:
                device_type = 'switch'
            else:
                device_type = 'unknown'

            # write data to dictionary
            if hostname:
                network_devices[hostname]['vendor'] = vendor
                network_devices[hostname]['model'] = model
                network_devices[hostname]['device_type'] = device_type

print
pprint.pprint(network_devices)
print
