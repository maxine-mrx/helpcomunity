#!/usr/bin/env python3

#############################################
#	Org: help comunity 		                #
#	Authors : BD and M4x1n3	                #
#	contribute: Rainel                      #     
#############################################
							# [help]Comunity#

import time, os
import optparse 

from urllib.parse import urljoin

try:
	import requests,pyfiglet

except Exception as err:
	print(err) 


from colors import *

from simple_crawler import *

from requesting import requester

from banner import banning



def sucess_banner():
	banner = pyfiglet.figlet_format('xsS-reflect', font="banner", justify="center")
	return banner


def test_error():
	err = '...'
	for _ in err:
		print(_, end='',flush=True)
		time.sleep(0.2)



def xsSR(mauroh,eddi):

	xss = False  

	input_name = find_input(eddi)


	with open('payloads',"r") as file:
	    payload = file.readlines()
	    payloads = list(map(lambda s: s.strip(), payload))

	for pay in payload:
		for param in input_name:
			tparams = []
			if param != None:
				tparams.append(param)
				for i in tparams:
					xparams='?'+str(i).lower()+'='+str(pay)
					urlAtack = urljoin(str(mauroh),xparams)
			#priequestnt(urlAtack)
			r = requests.get(urlAtack).content
			#print(urlAtack)
			#time.sleep(0.5)
		if 'maxine' in r.decode(): 
			
			print()
			print(f'{white}[~]{green} Form vulnerable xss (reflected) 🙃')
			print(f'{white}[*]{red} Payload to Atack:{white}{pay}')
			print(f'{white}[~]{blue} try this requests {urlAtack}')
			xss = True
			break
		
		else:
			test_error()
			#os.system('clear')			
		
	if xss:
		return sucess_banner()
	else:
		return xss


def usage():
	print('Usage: usagexssRD.py -u 10.10.10.10 -f wordlist.txt')



if __name__ == '__main__':


	parser = optparse.OptionParser("usage%prog -u <target> -f <payloads>")

	parser.add_option('-u','--url', dest='url', type='string',help='specify ip or site')

	parser.add_option('-f','--payloads', dest='payloads', type='string',help='specify dictionary file')

	(opt, args) = parser.parse_args()

	method = 'get'
	
	banning('m4x1n3')

	url = opt.url
	
	payloads = opt.payloads

	if not opt.url:
		print(f'{white}[~]{red} url not set.{white}[~]')


	if not opt.payloads:
		print(f'{white}[~]{red} set the payloads.{white}[~]')

	if not opt.payloads and  not opt.url:
		usage()	

	
	req = requester(url,method)
	print(req)
	
	mauroh, eddi = req
	
	xss=xsSR(mauroh,eddi)
	
	if xss:
		sucess_banner()


