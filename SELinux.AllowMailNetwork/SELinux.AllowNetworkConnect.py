'''
If getting following error:
ERROR: Failed to connect to server
Run as SUDO
Permissions for file from CLI to exe:
chmod +x SELinux.AllowNetworkConnect.py

'''

#!/usr/bin/python3

import subprocess

def get_status():
    # Execute the getsebool command and return the output
    result = subprocess.run(['getsebool', 'httpd_can_network_connect'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def set_status():
    # Execute the setsebool command
    subprocess.run(['setsebool', '-P', 'httpd_can_network_connect', '1'])

# Check the current status of httpd_can_network_connect
status = get_status()

if 'on' in status:
    print("allow network connect already on")
else:
    # If httpd_can_network_connect is off, turn it on
    set_status()
    print("turned on the allow allow network connect")