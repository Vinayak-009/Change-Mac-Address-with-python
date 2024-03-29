1.  How to change MAC 
    Basic approach

[
ifconfig eth0 down

ifconfig eth0 hw ether 00:11:22:33:44:55

ifconfig eth0 up
]




2. Using subprocess module :


#!/usr/bin/env python

import subprocess
subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:66", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
subprocess.call("ifconfig ", shell=True)





3. Using Variables:

#!/usr/bin/env python

import subprocess

interface = "eth0"
new_mac = "00:11:22:33:66:77"

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ifconfig ", shell=True)




4. Using Input Function :

#!/usr/bin/env python

import subprocess

interface = input("Enter your Interface: ")    #Use raw_input for python2
new_mac = input("Enter your new_mac: ")        #Use raw_input for python2

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ifconfig ", shell=True)


5. Using another subprocess.call Method :


#!/usr/bin/env python

import subprocess

interface = input("Enter your Interface: ")  # Use raw_input for python2
new_mac = input("Enter your new_mac: ")  # Use raw_input for python2

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call("ifconfig")



6. Command Line Arguments :


#!/usr/bin/env python

import subprocess
import optparse
parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")

parser.parse_args()

interface = input("Enter your Interface: ")  # Use raw_input for python2
new_mac = input("Enter your new_mac: ")  # Use raw_input for python2

print("[+] Changing MAC address for " + interface + "to" + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])


7. Initialising variables based on arguments:


#!/usr/bin/env python

import subprocess
import optparse
from optparse import OptionParser

parser: OptionParser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])



8. Using Functions :


#!/usr/bin/env python

import subprocess
import optparse
from optparse import OptionParser


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


parser: OptionParser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")

(options, arguments) = parser.parse_args()

change_mac(options.interface, options.new_mac)


9. Using Arguments:


#!/usr/bin/env python

import subprocess
import optparse
from optparse import OptionParser


def get_arguments():
    parser: OptionParser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")

    return parser.parse_args()


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)



10. Using Conditions:

#!/usr/bin/env python

import subprocess
import optparse
from optparse import OptionParser


def get_arguments():
    parser: OptionParser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error('[-] Please specify a new mac, use --help for more info.')

    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)



11. Using Algorithms:

	STEPS: 

1. Execute and read ifconfig
2. Read the MAC address from output
3. Check if MAC in ifconfig is what the user requested
4. print appropriate message


step 1:


#!/usr/bin/env python

import subprocess
import optparse
from optparse import OptionParser


def get_arguments():
    parser: OptionParser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error('[-] Please specify a new mac, use --help for more info.')

    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)




Step 2:


#!/usr/bin/env python

import subprocess
import optparse
from optparse import OptionParser
import re


def get_arguments():
    parser: OptionParser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error('[-] Please specify a new mac, use --help for more info.')

    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
# change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)

mac_address_search_result = mac_address_search_result = (re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode("utf-8")))

if mac_address_search_result:
    print(mac_address_search_result.group(0))
else:
    print("[-] Could not read MAC address.")

# print(mac_address_search_result.group(0))


Step 3:

 


#!/usr/bin/env python

import subprocess
import optparse
from optparse import OptionParser
import re


def get_arguments():
    parser: OptionParser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error('[-] Please specify a new mac, use --help for more info.')

    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = (re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode("utf-8")))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("CURRENT MAC = " + str(current_mac))

change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not changed.")



