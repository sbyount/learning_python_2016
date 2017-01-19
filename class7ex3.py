import re

def separate_interface_data(ospf_data):
    '''
    Take 'show ip ospf interface' data as a string
    Return a list corresponding to each section of the data
    (where a section pertains to one interface)
    ['interface1 ospf info', 'interface2 ospf info', etc ]
    '''

    # split the data
    ospf_data = re.split(r'(.+ is up, line protocol is up)', ospf_data)

    # dump any data before the first group
    ospf_data.pop(0)

    ospf_list = []

    while True:
        # if there are more than two items in the list
        if len(ospf_data) >= 2:
            # interface label for the section
            intf = ospf_data.pop(0)
            # section data
            section = ospf_data.pop(0)

            # put the string back together
            ospf_string = intf + section
            ospf_list.append(ospf_string)

        else:
            break
    return ospf_list

def generic_ospf_parser(pattern, ospf_data):
    '''
    Takes a generic regular expression pattern that has a group(1) match
    pattern and returns this
    Else returns None
    '''
    a_match = re.search(pattern, ospf_data)
    if a_match:
        return a_match.group(1)
    return None

def print_ospf_out(a_dict):
    '''
    Prints a given ospf interface section to STDOUT
    '''
    field_order = ('Int', 'IP', 'Area', 'Type', 'Cost', 'Hello', 'Dead')

    print
    for a_field in field_order:
        if a_dict.get(a_field) is not None:
            print "%15s:    %-20s" % (a_field, a_dict.get(a_field))


if __name__ == '__main__':

    f = open('ospf_data.txt')
    ospf_output = f.read()

    ospf_data_sections = separate_interface_data(ospf_output)
    f.close()

    # define patterns in a dict using regular expressions
    ospf_intf_patterns = {
        'Int'   : r"^(.+) is up, line protocol is up",
        'IP'    : r"Internet Address (.+?),",
        'Area'  : r"Internet Address .+?, Area (.+?), Attached",
        'Type'  : r", Network Type (.+?),",
        'Cost'  : r"Network Type .+?, Cost: (.+)",
        'Hello' : r"Timer intervals configured, Hello (.+?),",
        'Dead'  : r"Timer intervals configured, Hello .+?, Dead (.+?),",
    }

    for int_section in ospf_data_sections:

        tmp_dict = {}

        for k, ospf_pattern in ospf_intf_patterns.items():
            return_val = generic_ospf_parser(ospf_pattern, int_section)
            if return_val is not None:
                tmp_dict[k] = return_val

        print_ospf_out(tmp_dict)

print
