from distutils.command.config import config
import re
from this import d
from turtle import color
import libs.whoisinfo as whois
import libs.tracertinfo as trace
import libs.builtwithinfo as builtwith
import libs.waybackinfo as wayback
import libs.dnsinfo as dnsinfo
import pywebio
#from pywebio import start_server, config
from pywebio import pin
from pywebio.input import input, input_group, checkbox, TEXT
from pywebio.output import put_text, put_loading, put_row, put_code

#@config(theme='dark')
def execservice(domain, req_service): #Function containing situational definitions
    if 'whois' in req_service: #Pulling whois information
        w=whois.who(domain)
        put_text("WHOIS INFORMATION:\n", w)
        print("Whois successful")

    if 'traceroute' in req_service: #Pulling traceroute information
        t=trace.tracert(domain)
        put_text("TRACEROUTE INFORMATION:\n", t)
        print("Traceroute successful")

    if 'builtwith' in req_service: #Pulling builtwith information
        b=builtwith.bwith(domain)
        put_text("BUILTWITH INFORMATION:\n")
        for key in b:
            put_row([put_code(key),None,put_code(b[key])])        
        print("Builtwith successful")

    if 'wayback' in req_service: #Pulling information from the The Wayback MAcine
        w=wayback.wb(domain)
        put_text("WAYBACK INFORMATION:\n")
        put_text("Visit the following link:", w)

    if 'dnsinfo-A' in req_service: #Pulling Host Record information
        d=dnsinfo.dnsresolveA(domain)
        put_text("DNS INFORMATION (A Records):\n",d)

    if 'dnsinfo-MX' in req_service: #Pulling MX Record information
        d=dnsinfo.dnsresolveMX(domain)
        put_text("DNS INFORMATION (MX Records):\n",d)     


def reconserver(): #Function asking for user input and sorting the input data
    servicelist=['whois','traceroute','builtwith','wayback','dnsinfo-A','dnsinfo-MX']
    
    data= input_group(
        "Required Information",
        [
            input("Input domain name", name="domain", type=TEXT),
            checkbox("Services Required", name="servicedata",options=servicelist)
        ]
    )
#    print(data['servicedata'])
    domain=data['domain']
    print(domain)
    req_service=[]
    req_service=data['servicedata']
    execservice(domain, req_service) 
    

if __name__ == '__main__': #Function to run the reconserver function in a web server, Web app listens for connection on port 80
    pywebio.start_server(reconserver, port=80)    