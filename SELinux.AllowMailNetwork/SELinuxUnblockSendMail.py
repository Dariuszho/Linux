'''
If getting following error:
SMTP -> ERROR: Failed to connect to server: Permission denied (13)
Run as SUDO
Permissions for file from CLI to exe:
chmod +x SELinuxUnblockSendMail.py

'''

#!/usr/bin/python3

import subprocess

def get_status():
    # Execute the getsebool command and return the output
    result = subprocess.run(['getsebool', 'httpd_can_sendmail'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def set_status():
    # Execute the setsebool command
    subprocess.run(['setsebool', '-P', 'httpd_can_sendmail', '1'])

# Check the current status of httpd_can_sendmail
status = get_status()

if 'on' in status:
    print("send mail already on")
else:
    # If httpd_can_sendmail is off, turn it on
    set_status()
    print("turned on the allow send mail")
    