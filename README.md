A simple port scanner made in python.

Takes an ip address as a command line argument.

It is set to check for open ports on the first 1234 ports, which are generally the most interesting. It is pretty easy to change the 1234 to 65535 if necessary.

This was mainly a proof of concept for me, but was actually very fun to make, if a lot less complicated than initially believed.

Example useages:

>>> python port_scanner.py 127.0.0.1
>>> python port_scanner.py 74.125.201.103
>>> python post_scanner.py 192.168.1.40
