#!/usr/local/bin/python
__author__ = 'joshs@nyu.edu'
import sys, argparse, ipaddress

parser = argparse.ArgumentParser(description='This script will output dnsmanager commands for a new subnet creation')
parser.add_argument('-n','--network',help='Network to be used, i.e. 192.168.0.1/24',required=True)
parser.add_argument('-v','--vlan',help='VLAN index to be used, i.e. 201',required=True)
parser.add_argument('-c','--campus',help='Campus to be defined in. Options are nyuny,nyuad,nyush,etc',required=True)
parser.add_argument('-f','--firewalled',help='yes or no',required=True)
parser.add_argument('-fp','--firewallpair',help='Name of fw pair in use',required=False)

args = parser.parse_args()

print ("Network is: %s" % args.network)
print ("Vlan is: %s" % args.vlan)
print ("Campus is: %s" % args.campus)

net4 = ipaddress.ip_network(args.network)
vlan = args.vlan
campus = args.campus

# Network address assignment:
print "./dmgrcli.php --addptr --network=%s --ip=%s --ptrhostname=%s-vl%s-net --option_ip_status=net --disable_netrdb_checks --enable_reserve_ip_assignment" % (
    str(net4), str(net4[0]), str(campus), str(vlan))

# Broadcast assignment:
print "./dmgrcli.php --addptr --network=%s --ip=%s --ptrhostname=nyu-vl%s-bcast --option_ip_status=broadcast --disable_netrdb_checks --enable_reserve_ip_assignment" % (
    str(net4), str(net4[-1]), str(vlan))

# Router assignments:
print "./dmgrcli.php --newreg --nnlname=cos --nnfname=its --nntel=\"212-998-3444\" --nnemail=\"noc@nyu.edu\"  --option_ip_status=locked " \
      "--domain=net.nyu.edu --network=%s --ip=%s --hostname=nyu-vl%s-gw  --disable_netrdb_checks --enable_reserve_ip_assignment" % (
    str(net4), str(net4[1]), str(vlan))
print "./dmgrcli.php --newreg --nnlname=cos --nnfname=its --nntel=\"212-998-3444\" --nnemail=\"noc@nyu.edu\"  --option_ip_status=locked " \
      "--domain=net.nyu.edu --network=%s --ip=%s --hostname=primaryrtr-vl%s --disable_netrdb_checks --enable_reserve_ip_assignment" % (
    str(net4), str(net4[2]), str(vlan))
print "./dmgrcli.php --newreg --nnlname=cos --nnfname=its --nntel=\"212-998-3444\" --nnemail=\"noc@nyu.edu\"  --option_ip_status=locked " \
      "--domain=net.nyu.edu --network=%s --ip=%s --hostname=secondaryrtr-vl%s --enable_reserve_ip_assignment --disable_netrdb_checks" % (
    str(net4), str(net4[3]), str(vlan))

# Reserve firewalls:
print "./reserve_ipaddress.pl  --reserve --iplist=%s,%s --comment=\"Reserved for NOC usage\"" % (
    str(net4[4]), str(net4[-2]))
