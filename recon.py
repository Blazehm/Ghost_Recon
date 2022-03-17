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
import libs.iplocationinfo as iplocationinfo
import pywebio
from pywebio import *
#from pywebio import start_server, config
import pywebio.pin as pin
from pywebio.input import input, input_group, checkbox, TEXT
from pywebio.output import *


def execservice(domain, ipaddr, mailserver, req_service): #Function containing situational definitions

    if 'traceroute' in req_service: #Pulling traceroute information
        target_info_trace=trace.tracert(domain)
        for l in range(0,len(target_info_trace)):
            put_row(put_code(target_info_trace[l]['ip']), style(put_text("HOP"," ",str(l+1)," ",target_info_trace[l]['hostname']),'color: #70FF00'))
        print("Traceroute Success")    

    if 'dnsinfo-A' in req_service: #Pulling Host Record information
        target_info_dnsa=dnsinfo.dnsresolveA(domain)
        for l in range(0,len(target_info_dnsa)):
            put_row(put_code(target_info_dnsa[l]['data']),style(put_text("[Record "+str(l+1)+"] [Name: "+target_info_dnsa[l]['name']+"] [Class: "+target_info_dnsa[l]['class']+"]"),'color: #70FF00'))
        print('dnsA Successful')

    if 'dnsinfo-MX' in req_service: #Pulling MX Record information
        target_info_dnsmx=dnsinfo.dnsresolveA(domain)
        for l in range(0,len(target_info_dnsmx)):
            put_row(put_code(target_info_dnsmx[l]['data']),style(put_text("[Record "+str(l+1)+"] [Name: "+target_info_dnsmx[l]['name']+"] [Class: "+target_info_dnsmx[l]['class']+"]"),'color: #70FF00'))
        print('dnsA Successful')    

    if 'HTTP Headers' in req_service:
        target_info_headers=httpheaderinfo.headerinfo(domain) 
        for l in range(0,len(target_info_headers)):
            put_row(put_code(target_info_headers[l]['value']),style(put_text(target_info_headers[l]['name']),'color: #70FF00'))
        print('HTTP Headers success')

    if 'IP History' in req_service:
        target_info_iph=iphistoryinfo.iphistory(domain) 
        for l in range(0,len(target_info_iph)):
            put_row(put_code(target_info_iph[l]['ip']), style(put_text("[ Owner: "+target_info_iph[l]['owner']+"] [ location: "+target_info_iph[l]['location']+"] [ last seen: "+target_info_iph[l]['lastseen']),'color: #70FF00'))
        print('IP History success')

    if 'Reverse DNS Query' in req_service:
        target_info_rdns=rdnsinfo.info(ipaddr)
        put_row(put_code(target_info_rdns['response']['rdns']),style(put_text(target_info_rdns['query']['ip']),'color: #70FF00'))

    if 'Reverse MX Query' in req_service:
        target_info_rmx=reversemxinfo.mxinfo(mailserver)
        put_row(put_code(target_info_rmx['response']['domains']),style(put_text("Mailserver: "+   target_info_rmx['query']['mailserver']+" Domain Count: "+target_info_rmx['response']['domain_count']),'color: #70FF00'))

    if 'IP Location' in req_service:
        target_info_iploc=iplocationinfo.iploc(ipaddr)
        for key in target_info_iploc:
            put_row(put_code(target_info_iploc[key]),style(put_text(key),'color: #70FF00'))

config(title="Recon")

@config(theme='dark')
def reconserver(): #MAIN function
    servicelist=['traceroute','dnsinfo-A','dnsinfo-MX','HTTP Headers','IP History','IP Location','Reverse DNS Query','Reverse MX Query']
    iphistory='Shows a historical list of IP addresses a given domain name has been hosted on as well as where that IP address is geographically located, and the owner of that IP address.'
    iplocation='This tool will display geographic information about a supplied IP address including city, country, latitude, longitude and more.'
    reversedns='Find the reverse DNS entry (PTR) for a given IP. This is generally the server or host name.'
    reverseip='Takes a domain or IP address and quickly shows all other domains hosted from the same server. Useful for finding phishing sites or identifying other sites on the same shared hosting server. By default, the first 10,000 results are returned.'
    reversemx='Takes a mail server (e.g. mail.google.com) and quickly shows all other domains that use the same mail server. Useful for identifying domains that are used as email aliases'
    traceroute='Determines the series of servers that data traverses from the ViewDNS server to the specified domain name or IP address.'
    dnsrec='View all configured DNS records (A, MX, CNAME etc.) for a specified domain name.'
    http='Retrieves the HTTP headers of a remote domain. Useful in determining the web server (and version) in use and much more.'
    #traceinfo='What does Traceroute Do?'+'\n'+'A traceroute works by sending Internet Control Message Protocol (ICMP) packets, and every router involved in transferring the data gets these packets. The ICMP packets provide information about whether the routers used in the transmission are able to effectively transfer the data.'
    img = open('assests\LOGORECON-2-unscreen.gif', 'rb').read() 
    style(put_image(img),'border-radius: 8px; max-width: 50%; height: auto')
    style(put_text('IP Information Tools'), 'font-weight:bold; font-size: 30px;')
    style(
    put_tabs([
        #{'title':'Traceroute','content':''},
        #{'title':'DNS Record Lookup','content':''},
        #{'title':'Get HTTP Headers','content':''},
        {'title':'IP History','content':style(put_text(iphistory),'font-style: italic')},
        {'title':'IP Location Finder','content':style(put_text(iplocation),'font-style: italic')},
        #{'title':'Port Scanner','content':''},
        #{'title':'Reverse DNS','content':''},
        #{'title':'Reverse IP','content':''},
        #{'title':'Reverse MX','content':''},
        #{'title':'Reverse NS','content':''},
    ]),'color: #70FF00')
    style(put_text('Reverse Query Tools'), 'font-weight:bold; font-size: 30px;')
    style(
    put_tabs([
        #{'title':'Traceroute','content':''},
        #{'title':'DNS Record Lookup','content':''},
        #{'title':'Get HTTP Headers','content':''},
        #{'title':'IP History','content':''},
        #{'title':'IP Location Finder','content':''},
        #{'title':'Port Scanner','content':''},
        {'title':'Reverse DNS','content':style(put_text(reversedns),'font-style: italic')},
        {'title':'Reverse IP','content':style(put_text(reverseip),'font-style: italic')},
        {'title':'Reverse MX','content':style(put_text(reversemx),'font-style: italic')},
        #{'title':'Reverse NS','content':''},
    ]),'color: #70FF00')
    style(put_text('Network Information tools'), 'font-weight:bold; font-size: 30px;')
    style(
    put_tabs([
        {'title':'Traceroute','content':style(put_text(traceroute),'font-style: italic')},
        {'title':'DNS Record Lookup','content':style(put_text(dnsrec),'font-style: italic')},
        {'title':'Get HTTP Headers','content':style(put_text(http),'font-style: italic')},
        #{'title':'IP History','content':''},
        #{'title':'IP Location Finder','content':''},
        #{'title':'Port Scanner','content':''},
        #{'title':'Reverse DNS','content':''},
        #{'title':'Reverse IP','content':''},
        #{'title':'Reverse MX','content':''},
        #{'title':'Reverse NS','content':''},
    ]),'color: #70FF00')
    
    style(put_text("Recon Tools"), 'font-weight:bold; font-size: 30px;')
    
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