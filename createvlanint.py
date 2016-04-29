#!/usr/local/bin/python
__author__ = 'joshs@nyu.edu'
import argparse
import ipaddress

parser = argparse.ArgumentParser(description='This script will output required SVI interface config')
parser.add_argument('-n', '--network', help='Network to be used, i.e. 192.168.0.1/24', required=True)
parser.add_argument('-v', '--vlan', help='VLAN index to be used, i.e. 201', type=int, required=True)
parser.add_argument('-vg', '--vrrp', help='VRRP group to be used, i.e. 41', type=int, required=True)
parser.add_argument('-d', '--description', help='Description', type=int, required=True)

args = parser.parse_args()

print ('Network is: %s' % args.network)
print ('Vlan is: %s' % args.vlan)
print ('VRRP group is: %s\n\n' % args.vrrp)

net4 = ipaddress.ip_network(args.network)
vlan = args.vlan
vrrp = args.vrrp

print("# Primary router:")
print("vlan %s" % str(vlan))
print("\tname %s" % str(net4))

def print_int():
    print("\ninterface vlan%s" % str(vlan)
          "\tdescription")
