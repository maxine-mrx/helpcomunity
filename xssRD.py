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
except :
	print('install modules! please read readme')

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
	


def xsSR(a,b):

	xss = False
	
	check_form_method = find_form(b)  # get form method  
	
	input_name = find_input(b)
	

	with open('payloads',"r") as file:
	    payload = file.readlines()
	    payloads = list(map(lambda s: s.strip(), payload))

	for pay in payload:
		for param in input_name:
			if param != None:
				tparams = param
				xparams='?'+str(tparams).lower()+'='+str(pay)
				#print(f'{green}[+] {white}Parameters found:{green}{tparams}', end='', sep=' <;>')
				#print()
			
				urlAtack = urljoin(str(a),xparams)
			#print(urlAtack)
			
		req = requests.get(urlAtack,#cookies=cookies
                ).content
		#print(req)	
		if 'maxine' in req.decode(): 
			print()
			print(f'{white}[~]{green} Form vulnerable xss (reflected) 🙃')
			print(f'{white}[*]{red} Payload to Atack:{white}{pay}')
			print(f'{white}[~]{blue} try this requests {urlAtack}')
			xss = True
			break
		
		else:
			test_error()
			os.system('clear')			
	if xss :
		return sucess_banner()
	else:
		return xss

def usage():
	print('Usage: xssRD.py -u 10.10.10.10 -f payloads')



if __name__ == '__main__':


	parser = optparse.OptionParser("usage%prog -u <target> -f <payloads>")

	parser.add_option('-u','--url', dest='url', type='string',help='specify ip or site')

	parser.add_option('-f','--payloads', dest='payloads', type='string',help='specify dictionary file')

	(opt, args) = parser.parse_args()

	method = 'get'
	
	#cookies = dict(PHPSESSID='fbcd200irn3boacre2701rvtr7',security="low")
	
	banning('m4x1n3')

	url = opt.url
	
	payloads = opt.payloads

	if not opt.url:
		print(f'{white}[~]{red} url not set.{white}[~]')


	if not opt.payloads:
		print(f'{white}[~]{red} set the payloads.{white}[~]')

	if not opt.payloads and  not opt.url:
		usage()	

	
	req = requester(url,method,cookies=cookies)
	print(req)
	mauroh, eddi = req
	xss=xsSR(mauroh,eddi)
	
	if xss:
		sucess_banner()
		print(xss)

