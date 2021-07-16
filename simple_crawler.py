#!/usr/bin/env python3


#############################################
#	Org: help comunity 		                #
#	Authors : BD and M4x1n3	                #
#	contribute: Rainel                      #     
#############################################
							# [help]Comunity#



from bs4 import BeautifulSoup as beaut

from requesting import requester 

import requests


def find_form(req):
	
	data = req.content
	soup = beaut(data,'html.parser')
	form = soup.find_all('form')
	
	#fmethod = soup.form[0].attrs.get('method')
	
	return form #, fmethod


def find_links(links):
	get_links = []
	data = req.text
	soup = beaut(data,'html.parser')
	links = soup.find_all('a')
	for link in links:
		if link.get('href'):
			get_links.append(link.get('href'))
			if '=' in link.get('href'):
				print(link.get('href'))	 
				
	return get_links



def find_input(req):
	imputs_names=[]
	
	data = req.content
	soup = beaut(data,'html.parser')
	imput = soup.find_all('input')

	for i in imput:
		imputs_names.append(i.attrs.get('name'))
	
	return imputs_names

def find_select(req):
	
	selects_names=[]
	data = req.content
	soup = beaut(data,'html.parser')
	select = soup.find_all('select')

	for i in select:
		selects_names.append(i.attrs.get('name'))
	
	return selects_names	

if __name__ == '__main__':
	
	pass
