# imports
import pprint
import sys

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

# initialize outer dictionary
network_devices = {}

# for each device data set
for cdp_data in cdp_neighbors:

    # split the data set into lines
    cdp_data_line = cdp_data.split('\n')

    # set router_name to null for each loop
    remote_hostname = ''
    local_hostname = ''

    # for each line in a device blob
    for line in cdp_data_line:

        # set hostname to '' at header
        if '-------------------------' in line:
            remote_hostname = ''

        if 'show cdp neighbors detail' in line:
            local_hostname = line.split('show cdp neighbors detail')[0]
            if '>' in local_hostname:
                local_hostname = local_hostname.split('>')[0]
            elif '#' in local_hostname:
                local_hostname = local_hostname.split('#')[0]
            else:
                sys.exit('Invalid prompt for local hostname - exiting')

            # if you find a new device, initilize it as a blank directory
            if not local_hostname in network_devices:
                network_devices[local_hostname] = {}


        # get the router_name if it is in the line
        if 'Device ID: ' in line:
            (junk, remote_hostname) = line.split('Device ID: ')
            remote_hostname = remote_hostname.strip()

            # the first time through, initialize the inner dictionary
            if not remote_hostname in network_devices:
                network_devices[remote_hostname] = {}

            # map adjacencies
            if (local_hostname in network_devices) and remote_hostname:

                # add adjacency field if it does not exist
                if not 'adjacent_devices' in network_devices[local_hostname]:
                    network_devices[local_hostname]['adjacent_devices'] = [remote_hostname]

                # if already present, append to the list
                else:
                    if not remote_hostname in network_devices[local_hostname]['adjacent_devices']:
                        network_devices[local_hostname]['adjacent_devices'].append(remote_hostname)

        # get ip address if it is in the line
        if 'IP address: ' in line:
            (junk, ip) = line.split('IP address: ')
            ip = ip.strip()

            if remote_hostname:
                network_devices[remote_hostname]['ip'] = ip

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
            if remote_hostname:
                network_devices[remote_hostname]['vendor'] = vendor
                network_devices[remote_hostname]['model'] = model
                network_devices[remote_hostname]['device_type'] = device_type

print
pprint.pprint(network_devices)
print
