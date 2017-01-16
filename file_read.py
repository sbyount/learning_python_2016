# read in the variables from the cdp data file
from cdp_data import (sw1_show_cdp_neighbors_detail,
r1_show_cdp_neighbors_detail,
r2_show_cdp_neighbors_detail,
r3_show_cdp_neighbors_detail,
r4_show_cdp_neighbors_detail,
r5_show_cdp_neighbors_detail)

DEBUG = False

# put cdp data in a list
cdp_neighbors = (
    sw1_show_cdp_neighbors_detail,
    r1_show_cdp_neighbors_detail,
    r2_show_cdp_neighbors_detail,
    r3_show_cdp_neighbors_detail,
    r4_show_cdp_neighbors_detail,
    r5_show_cdp_neighbors_detail,
)

if DEBUG:
    print cdp_neighbors[0]

# for each device data set
for cdp_data in cdp_neighbors:

    # split the data set into lines
    cdp_data_line = cdp_data.split('\n')

    # for each line in a device
    for line in cdp_data_line:

        # set router_name to null for each loop
        router_name = ''

        # get the router_name if it is in the line
        if 'Device ID: ' in line:
            (junk, router_name) = line.split('Device ID: ')
            print router_name

        # get ip address if it is in the line
        if 'IP address: ' in line:
            (junk, ip) = line.split('IP address: ')
