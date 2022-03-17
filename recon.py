from distutils.command.config import config
from msilib.schema import RadioButton
import re
from this import d
from turtle import color
import libs.tracertinfo as trace
import libs.dnsinfo as dnsinfo
import libs.httpheaderinfo as httpheaderinfo
import libs.iphistoryinfo as iphistoryinfo
import libs.rdnsinfo as rdnsinfo
import libs.reversemxinfo as reversemxinfo
import pywebio
#from pywebio import start_server, config
import pywebio.pin as pin
from pywebio.input import input, input_group, checkbox, TEXT
from pywebio.output import *

#@config(theme='dark')
def execservice(domain, ipaddr, mailserver, req_service): #Function containing situational definitions

    if 'traceroute' in req_service: #Pulling traceroute information
        target_info_trace=trace.tracert(domain)
        for l in range(0,len(target_info_trace)):
            put_row(put_code(target_info_trace[l]['ip']), put_text("HOP"," ",str(l+1)," ",target_info_trace[l]['hostname']))
        print("Traceroute Success")    

    if 'dnsinfo-A' in req_service: #Pulling Host Record information
        target_info_dnsa=dnsinfo.dnsresolveA(domain)
        for l in range(0,len(target_info_dnsa)):
            put_row(put_code(target_info_dnsa[l]['data']),put_text("[Record "+str(l+1)+"] [Name: "+target_info_dnsa[l]['name']+"] [Class: "+target_info_dnsa[l]['class']+"]"))
        print('dnsA Successful')

    if 'dnsinfo-MX' in req_service: #Pulling MX Record information
        target_info_dnsmx=dnsinfo.dnsresolveA(domain)
        for l in range(0,len(target_info_dnsmx)):
            put_row(put_code(target_info_dnsmx[l]['data']),put_text("[Record "+str(l+1)+"] [Name: "+target_info_dnsmx[l]['name']+"] [Class: "+target_info_dnsmx[l]['class']+"]"))
        print('dnsA Successful')    

    if 'HTTP Headers' in req_service:
        target_info_headers=httpheaderinfo.headerinfo(domain) 
        for l in range(0,len(target_info_headers)):
            put_row(put_code(target_info_headers[l]['value']),put_text(target_info_headers[l]['name']))
        print('HTTP Headers success')

    if 'IP History' in req_service:
        target_info_iph=iphistoryinfo.iphistory(domain) 
        for l in range(0,len(target_info_iph)):
            put_row(put_code(target_info_iph[l]['ip']), put_text("[ Owner: "+target_info_iph[l]['owner']+"] [ location: "+target_info_iph[l]['location']+"] [ last seen: "+target_info_iph[l]['lastseen']))
        print('IP History success')

    if 'Reverse DNS Query' in req_service:
        target_info_rdns=rdnsinfo.info(ipaddr)
        put_row(put_code(target_info_rdns['response']['rdns']),put_text(target_info_rdns['query']['ip']))

    if 'Reverse MX Query' in req_service:
        target_info_rmx=reversemxinfo.mxinfo(mailserver)
        put_row(put_code(target_info_rmx['response']['domains']),put_text("Mailserver: "+target_info_rmx['query']['mailserver']+" Domain Count: "+target_info_rmx['response']['domain_count']))


def reconserver(): #MAIN function
    servicelist=['traceroute','dnsinfo-A','dnsinfo-MX','HTTP Headers','IP History','Reverse DNS Query','Reverse MX Query']

    #traceinfo='What does Traceroute Do?'+'\n'+'A traceroute works by sending Internet Control Message Protocol (ICMP) packets, and every router involved in transferring the data gets these packets. The ICMP packets provide information about whether the routers used in the transmission are able to effectively transfer the data.'
    put_image("D:\GitHub\Ghost_Recon\assests\logo_idea.png")
    put_text("Learn about Recon Tools")
    put_tabs([
        {'title':'traceroute','content':''},
        {'title':'DNS Record Lookup','content':''},
        {'title':'Get HTTP Headers','content':''},
        {'title':'IP History','content':''},
        {'title':'IP Location Finder','content':''},
        {'title':'Port Scanner','content':''},
        {'title':'Reverse DNS','content':''},
        {'title':'Reverse IP','content':''},
        {'title':'Reverse MX','content':''},
        {'title':'Reverse NS','content':''},
    ])
    
    put_text("Use the Recon Tools")
    
    data= input_group(
        "Recon Tools",
        [
            input("Input domain name", name="domain", type=TEXT),
            input("Input IP Address (for Reverse DNS)", name='IP', type=TEXT),
            input("Input mail server (for Reverse MX)", name='mailserver', type=TEXT),
            checkbox("Services Required", name="servicedata",options=servicelist)
        ]
    )
    
#    print(data['servicedata'])
    domain=data['domain']
    ipaddr=data['IP']
    mailserver=data['mailserver']
    print(domain)
    print(ipaddr)
    print(mailserver)
    req_service=[]
    req_service=data['servicedata']
    execservice(domain, ipaddr, mailserver, req_service)
    

if __name__ == '__main__': #Function to run the reconserver function in a web server, Web app listens for connection on port 80
    pywebio.start_server(reconserver, port=80)    