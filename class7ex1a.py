import re
from pprint import pprint

def generic_cdp_parser(pattern, cdp):
    '''
    Search for pattern in cdp data
    return relevant .group(1)
    else return ''
    '''

    # break the data into lines
    cdp = cdp.split('\n')

    for line in cdp:
        #search for pattern
        re_pattern = re.search(pattern, line)

        # return match if found
        if re_pattern:
            return_val = re_pattern.group(1)
            return return_val.strip()

    return ''

# allows importrable and executable code to exist
if __name__ == '__main__':

    # open the file
    cdp_file = 'r1_cdp.txt'
    f = open(cdp_file)

    # read cdp data into a list, and close file
    cdp_data = f.read()
    f.close()

    # initialize blank dictionary
    network_devices = {}

    # look for device id and put chars that follow into the dictionary
    network_devices['remote_hostname'] = generic_cdp_parser(r'Device ID: (.+)', cdp_data)
    # look for ip addr and put chars that follow into the dictionary
    network_devices['ip'] = generic_cdp_parser(r'IP address: (.+)', cdp_data)
    # look for platform only at begin line, and put the text that follows into vendor, only once
    network_devices['vendor'] = generic_cdp_parser(r'^Platform: (.+?) ', cdp_data)
    # look for platform only at begin line, skip the first word after, get the next blob
    network_devices['model'] =  generic_cdp_parser(r'^Platform: \w+ (.+),', cdp_data)
    # look for capabilities, and put the first word after than in device_type
    network_devices['device_type'] = generic_cdp_parser(r'^Platform: .+Capabilities: (.+?) ', cdp_data)

    print
    pprint(network_devices)
