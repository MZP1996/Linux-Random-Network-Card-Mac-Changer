#! /usr/bin/env python

import subprocess
import Mac_Randomizer

interface = input("What is The name of your network: ")
New_Mac = Mac_Randomizer.generate_mac_address()

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + New_Mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

print("Your new Mac Address is: " + New_Mac)