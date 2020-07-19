#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:52:30 2020
"""

import requests
import re
import requests
from bs4 import BeautifulSoup


# Step 1) Find the public IP of the user. This is easier said that done, look into the library Netifaces if you're
# interested in getting the public IP locally.
# The GeoIP API I'm going to use here is 'https://geojs.io/' but any service offering similar JSON data will work.

ip_request = requests.get('https://get.geojs.io/v1/ip.json')
my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
print(my_ip)
# Prints The IP string, ex: 198.975.33.4

# Step 2) Look up the GeoIP information from a database for the user's ip
#my_ip="106.67.15.107"
geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
geo_request = requests.get(geo_request_url)
geo_data = geo_request.json()
#print(geo_data)
print("Welcome to ",geo_data['city'])    
    

def search():
    getpage=requests.get("https://www.google.com/search?q=santa+barbara+latest+woman+health+news&oq=santa+barbara+latest+woman+health+news&aqs=chrome.0.69i59.3983j0j7&sourceid=chrome&ie=UTF-8")
    getpage_soup= BeautifulSoup(getpage.text, 'html.parser')
    
    all_links= getpage_soup.findAll('a')
    l=[]
    for link in all_links:
        l.append(link)
    myOnDict=[]
    for i in l:
        p=re.compile('href=\"(.*?)\"')
        #print(i)
        r1=p.findall(str(i))
        myOnDict.append(r1[0])
   
    myOneDict2=[]
    for j in myOnDict:
        p2=re.compile('(https://.*?)&')
        #print(i)
        r12=p2.findall(str(j))
        myOneDict2.append(r12)
        
    #print(myOneDict2)
    list2 = [x for x in myOneDict2 if x]
        
    link_list = []
    for each_url in list2[1:]:
        link_string = '<a href = "'
        link_string = link_string + each_url[0]
        link_string = link_string +'">' 
        link_name = each_url[0].split('.')[1]
        link_string = link_string + link_name + '</a><br>\n'
        link_list.append(link_string)
    
    
    outref = open("/Users/lilyhe/Desktop/mytemp.htm",'w')
    outref.writelines(link_list)
    outref.close() 

    return ''.join(link_list)
