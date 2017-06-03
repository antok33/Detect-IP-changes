from json import load
from urllib2 import urlopen
from time import gmtime, strftime
import time
import sys


def ip():
	with open('output.txt', 'a') as log:	
		timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		my_ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
		log.write("\n")
		log.write("Time: " + timestamp)
		log.write("\n")
		log.write("IP: " + my_ip)
		log.write("\n")
		log.write("++++++++++++")
		log.write("\n")
		log.write("++++++++++++")
		
		print "Time: ", timestamp
		print "IP: ", my_ip
		print "++++++++++++"
	
if len(sys.argv) == 2:
	secs = int(sys.argv[1])	
	while True:
		ip()
		time.sleep(secs)
else:
	print "Wrong execution......."
	print "You have to define in how many seconds you want to check the ip"
	print "=============================="
	print "For example: python public_ip 20"
	print "Checking ip every 20 secs"
	print "Results to output.txt"
