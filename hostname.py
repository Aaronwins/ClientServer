#!/usr/bin/python

import subprocess

hostnameprint = subprocess.check_output("hostname", shell=True)
hostnameprint = hostnameprint.decode("ascii")
ip_addresses =  subprocess.check_output("hostname -I", shell=True)
ip_addresses = ip_addresses.decode("ascii")

plus = "++++++++++++++++++++++++++++++++++++++++++++++++++++"
print(plus)

print("")
print("")
print("")

print("Hostname: ",hostnameprint)

print("")
print("")
print("")


listip_addresses = ip_addresses.split()
print("Valid addresses:")
for i,address in enumerate(listip_addresses):
        number = i + 1
        print(number,":",address)