#!/bin/bash

:<<'COMMENT'
If getting following error:
ERROR: Failed to connect to server
Run as SUDO
Permissions for file from CLI to exe:
chmod +x SELinux.AllowNetworkConnect.sh
COMMENT

# Check the current status of httpd_can_network_connect
status=$(getsebool httpd_can_network_connect)

if [[ "$status" == *"on"* ]]; then
    echo "allow network connect on"
else
    # If httpd_can_network_connect is off, turn it on
    setsebool -P httpd_can_network_connect 1
    echo "turned on the allow network connect"
fi



