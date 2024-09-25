#!/usr/bin/python

import subprocess

output = subprocess.check_output("hostname -I", shell=True)
output = output.decode("ascii")


print(output)
ip_addresses = output.split()
print(ip_addresses)


for i in ip_addresses:
        print(i)