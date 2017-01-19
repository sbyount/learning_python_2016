import pprint

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

uptime_dict = {}

uptime_list = (uptime1, uptime2, uptime3, uptime4)

for line in uptime_list:

    # get device name
    uptime_dict['device_name'] = line.split()[0]

    # get years
    if 'years' in line:
        uptime_years = line.split(' years ')[-1]

    # get weeks
    if 'weeks' in line:
        uptime_weeks = line.split(' weeks ')[-1]

    # get days
    if 'days' in line:
        update_days = line.split(' days ')[-1]

    # get hours
    if 'hour' in line:
        uptime_hours = line.split(' hours ')[-1]

    # get minutes
    if 'minutes' in line:
        uptime_minutes = line.split(' minutes ')[-1]

print uptime_dict
