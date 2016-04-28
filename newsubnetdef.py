#!/usr/local/bin/python
__author__ = 'joshs@nyu.edu'
import sys, argparse, ipaddress

parser = argparse.ArgumentParser(description='This script will output dnsmanager commands for a new subnet creation')
parser.add_argument('-n','--network',help='Network to be used, i.e. 192.168.0.1/24',required=True)
parser.add_argument('-v','--vlan',help='VLAN index to be used, i.e. 201',required=True)
parser.add_argument('-c','--campus',help='Campus to be defined in. Options are nyuny,nyuad,nyush,etc',required=True)
args = parser.parse_args()

print ("Network is: %s" % args.network)
print ("Vlan is: %s" % args.vlan)
print ("Campus is: %s" % args.campus)

net4 = ipaddress.ip_network(args.network)
vlan = args.vlan
campus = args.campus

print "# Network address assignment:"
print "./dmgrcli.php --addptr --network=" + str(net4) + " --ip=" + str(net4[0]) + " --ptrhostname=" + str(campus) + "-vl" + str(vlan) + "-net --option_ip_status=net --disable_netrdb_checks --enable_reserve_ip_assignment"
print "# Broadcast assignment:"
print "./dmgrcli.php --addptr --network=" + str(net4) + " --ip=" + str(net4[-1]) + " --ptrhostname=nyu-vl" + str(vlan) + "-bcast --option_ip_status=broadcast --disable_netrdb_checks --enable_reserve_ip_assignment"
print "# Router assignments:"
print "./dmgrcli.php --newreg --nnlname=cos --nnfname=its --nntel=\"212-998-3444\" --nnemail=\"noc@nyu.edu\"  --option_ip_status=locked --domain=net.nyu.edu --network=" + str(net4) + " --ip=" + str(net4[1]) + " --hostname=nyu-vl" + str(vlan) + "-gw  --disable_netrdb_checks --enable_reserve_ip_assignment"
print "./dmgrcli.php --newreg --nnlname=cos --nnfname=its --nntel=\"212-998-3444\" --nnemail=\"noc@nyu.edu\"  --option_ip_status=locked --domain=net.nyu.edu --network=" + str(net4) + " --ip=" + str(net4[2]) + " --hostname=primaryrtr-vl" + str(vlan) + " --disable_netrdb_checks --enable_reserve_ip_assignment"
print "./dmgrcli.php --newreg --nnlname=cos --nnfname=its --nntel=\"212-998-3444\" --nnemail=\"noc@nyu.edu\"  --option_ip_status=locked --domain=net.nyu.edu --network=" + str(net4) + " --ip=" + str(net4[3]) + " --hostname=secondaryrtr-vl" + str(vlan) + " --enable_reserve_ip_assignment --disable_netrdb_checks"
print "# Reserve firewall:"
print "./reserve_ipaddress.pl  --reserve --iplist=" + str(net4[4]) + "," + str(net4[-2]) + " --comment=\"Reserved for NOC usage\""
