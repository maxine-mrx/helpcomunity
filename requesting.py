#!/usr/bin/env python3

#############################################
#	Org: help comunity 		                #
#	Authors : DB and M4x1n3	                #	
#############################################



import os

import requests

from colors import red,green,blue,white





def requester(url,method):
	
	
	'''
		esta func simplesmente trata o parametro url, method eu useu http: 
		pork os testes foram locais mude a linha 28 e 29 conforme o comentario
		se necessario uma vez que alguns sites fazem redirecioamento automatico 
		para requisiçoes http para https ex: http//:free.facebook.com vai ir em https...
		kkkkkkkkkkkkkkkkkkkkk me perdi no codigo :)

	'''
	
	#################  url check  ################
	
	if not url.startswith('https://'): # if not url.startswith('https://'):
		url = 'https://'+ str(url)    # url = 'https://' + str(url)

	if not url.endswith('/'):
		url = str(url)+ '/'
	
	################ Method check ################

	
	if method == 'get' or method == 'GET':
		req = requests.get(url)


	elif method == 'post' or method == 'POST':
		req = requests.post(url)
		
	else:
		req ='{} method not suport ...'.format(red)
		print(req)

	################ Header check ################
	
	
	header = input('{} [~] Verificate Header Response ? (Y | N ) [~]: '.format(blue))
	

	if header == 'y' or header == 'Y':
		for header,value in req.headers.items():
			print(f'{green}{header} :{white}{value}') 
		print(f'{green}State-Code:{white}{req.status_code}')
	else:
		pass

	

	return [url , req]

if __name__ == '__main__':
	
	#print(requester('https://xss-game.appspot.com/level1/','get'))
	pass
