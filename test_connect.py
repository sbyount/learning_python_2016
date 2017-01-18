from netmiko import ConnectHandler
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("my_log")
logger.debug('This message should go to the log file')


cisco_1002x = {
    'device_type': 'cisco_ios',
    'ip':   '10.9.18.38',
    'username': 'zg46503',
    'password': '*******',
    'port' : 22,          # optional, defaults to 22
    'secret': '',     # optional, defaults to ''
    'verbose': False,       # optional, defaults to False
    'global_delay_factor': 4,                # Try 2 and then 4
}

cisco_1921 = {
    'device_type': 'cisco_ios_telnet', # use telnet instead of ssh
    'ip':   '10.192.64.190',
    'username': 'netsupport',
    'password': 'why1stacacsd0wn',
    'port' : 23,          # optional, defaults to 22
    'secret': '',     # optional, defaults to ''
    'verbose': False,       # optional, defaults to False
}

cisco_3945 = {
    'device_type': 'cisco_ios',
    'ip':   '10.192.65.35',
    'username': 'netsupport',
    'password': 'why1stacacsd0wn',
    'port' : 22,          # optional, defaults to 22
    'secret': '',     # optional, defaults to ''
    'verbose': False,       # optional, defaults to False
}

net_connect = ConnectHandler(**cisco_1002x)
#net_connect.send_command('\n')
output = net_connect.send_command('show ip int brief')
print(output)
