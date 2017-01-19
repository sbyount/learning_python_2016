#  Run the package "show_version"

import show_version

def main():

    with open('show_version.txt', 'r') as version_file:
        show_ver = version_file.read()

    model = show_version.obtain_model(show_ver)
    os_version = show_version.obtain_os_version(show_ver)
    uptime = show_version.obtain_uptime(show_ver)

    print
    print '%15s: %-50s' % ('Model', model)
    print '%15s: %-50s' % ('OS Version', os_version)
    print '%15s: %-50s' % ('Uptime', uptime)
    print

if __name__ == '__main__':
    main()
