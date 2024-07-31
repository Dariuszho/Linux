#!/bin/bash

:<<'COMMENT'
If getting following error:
SMTP -> ERROR: Failed to connect to server: Permission denied (13)
Run as SUDO
Permissions for file from CLI to exe:
chmod +x SELinuxUnblockSendMail.sh
COMMENT

# Check the current status of httpd_can_sendmail
status=$(getsebool httpd_can_sendmail)

if [[ "$status" == *"on"* ]]; then
    echo "send mail already on"
else
    # If httpd_can_sendmail is off, turn it on
    setsebool -P httpd_can_sendmail 1
    echo "turned on the allow send mail"
fi



