import subprocess
interface = raw_input("interface >")
new_mac = raw_input("new_mac >")
print("[+] changing MAC address for " + interface + "to" + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac ])
subprocess.call(["ifconfig", interface, "up"])


