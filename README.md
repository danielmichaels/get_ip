# get_ip
Using an API get the interfaces external IP address.

## What
<<<<<<< HEAD
Using the ('https://api.ipify.org')[ipify] API this script will with the help
=======
Using the ['https://api.ipify.org'](ipify) API this script will with the help
>>>>>>> c83a43d0b4cbeae093d0894892ec19a94c8a846e
of the `requests` library pull in the interfaces external IP address. 

Additionally, it will create a CSV file with the IP address and DateTime that
the script was run. The CSV is prepended with headers to match.

## Why
- check when interface changes IP; particularly if using VPN or dynamic IP,
- coupled with a speedtester, categorise the IP addresses by speed,
- check that VPN or Proxy is actually configured, or running as expected.

## Requirements
- requests==2.18.4
