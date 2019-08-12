#!/usr/bin/python2.7
#Coded by Sha2ya3n
# MAC changer is a program to changes your mac address and allows you to pick any other MAC address!
# it useful for any kind of program that u do not want to any body knows your mac-address or access somewhere with particular MAC-address

import subprocess
import optparse
import re

def macchanger(interface,new_mac):
    subprocess.call(["ifconfig", interface,"hw","ether", new_mac])
    subprocess.call(["ifconfig", interface,"down"])
    subprocess.call(["ifconfig", interface,"up"])

def get_argumet():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Insert your interface that you wanna change its MAC address!")
    parser.add_option("-m", "--macaddress", dest="new_mac", help="Insert your MAC address that you wanna change it!")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error ("[-] Enter your interface that u wanna change its MAC address")
    elif not options.new_mac:
        parser.error ("[-] Enter your MAC address that u wanna change it")
    return options

def get_mac(interface):
    ifconf = subprocess.check_output(["ifconfig", interface])
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconf)
    if current_mac:
        return current_mac.group(0)
    elif not current_mac:
        print "[-] MAC address that u entered was not correct check it out again!"
        return None

options = get_argumet()
macchanger(options.interface,options.new_mac)

current_mac = get_mac(options.interface)
if current_mac == options.new_mac:
    print "[+] MAC address is changed sucssfully \n%s"%options.new_mac
else:
    print "[-] MAC Adress dose not changed succssesfuly"
