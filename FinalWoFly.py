#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:52:30 2020

@author: xinyuehu
"""

"""import requests
g=requests.get("https://www.google.com/search?q=santa+barbara+health+news&client=safari&rls=en&sxsrf=ACYBGNSh5z-zUdyCUd9zw0yJaI3OjEW92Q:1579401069727&ei=bb8jXvL9K8r1-gSdoLS4Bg&start=0&sa=N&ved=2ahUKEwiy6N-9z47nAhXKup4KHR0QDWc4ChDx0wN6BAgMECw&biw=1470&bih=876")
r=g.text
for child in r.findAll('a'): 
    print(child)
"""
#Welcome message while entering new geolocation

import requests
import re
import requests
from bs4 import BeautifulSoup
# import pyrebase

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
    #getpage= requests.get('https://www.google.com/search?q=santa+barbara+health+news&client=safari&rls=en&sxsrf=ACYBGNSh5z-zUdyCUd9zw0yJaI3OjEW92Q:1579401069727&ei=bb8jXvL9K8r1-gSdoLS4Bg&start=0&sa=N&ved=2ahUKEwiy6N-9z47nAhXKup4KHR0QDWc4ChDx0wN6BAgMECw&biw=1470&bih=876')
    getpage=requests.get("https://www.google.com/search?q=santa+barbara+latest+woman+health+news&oq=santa+barbara+latest+woman+health+news&aqs=chrome.0.69i59.3983j0j7&sourceid=chrome&ie=UTF-8")
    getpage_soup= BeautifulSoup(getpage.text, 'html.parser')
    
    all_links= getpage_soup.findAll('a')
    l=[]
    for link in all_links:
        l.append(link)
        #print("\n")
        #print (link)
    #print(len(l))
        
    
    myOnDict=[]
    for i in l:
        p=re.compile('href=\"(.*?)\"')
        #print(i)
        r1=p.findall(str(i))
        myOnDict.append(r1[0])
    #print(l[14:20])
    
    #print("........................................\n")
    #print(myOnDict[14:20])
    myOneDict2=[]
    for j in myOnDict:
        p2=re.compile('(https://.*?)&')
        #print(i)
        r12=p2.findall(str(j))
        myOneDict2.append(r12)
        
    #print(myOneDict2)
    list2 = [x for x in myOneDict2 if x]
    #print(list2)
    #print(len(list2))  
    #sending urls to firebase database
    
#     config = {
#       "apiKey": "AIzaSyAtignXhKRuczQvRI3l5xWqdsUufmSlAgM",
#       "authDomain": "flywo-39f90.firebaseapp.com",
#       "databaseURL": "https://flywo-39f90.firebaseio.com",
#       "storageBucket": "flywo-39f90.appspot.com"
#     }
    
#     firebase = pyrebase.initialize_app(config)
    #print(fullurl)
#     db = firebase.database()
#     i=0
#     for url in list2[1:]:
#         #print(url)
#         i=i+1
#         db.child("Articles").child(i).set(url[0])
        
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




  
    
"""for k in list2[1:]:
    r="<a href="\"
    r2=""</a>"
    
    print(r+k[0]+r2)"""
#code to open URLS    
"""import webbrowser

for url in list2[1:]:
    webbrowser.open_new_tab(url[0])"""