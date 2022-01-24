from turtle import color
import libs.whoisinfo as whois
import libs.tracertinfo as trace
import pywebio
from pywebio.input import input, input_group, checkbox, FLOAT, TEXT
from pywebio.output import put_text, put_table, put_file, put_loading


def execservice(domain, req_service):
    if 'whois' in req_service:
        w=whois.who(domain)
        with put_loading(shape='border', color='primary'):
            put_text("WHOIS INFORMATION:\n", w)
            print("END")

    if 'traceroute' in req_service:
        t=trace.tracert(domain)
        with put_loading(shape='border', color='primary'):
            put_text("TRACEROUTE INFORMATION:\n", t)
            print("END")


def reconserver():
    servicelist=['whois','traceroute']
    
    data= input_group(
        "Required Information",
        [
            input("Input domain name", name="domain", type=TEXT),
            checkbox("Services Required", name="servicedata",options=servicelist)
        ]
    )
#    print(data['servicedata'])
    domain=data['domain']
    req_service=[]
    req_service=data['servicedata']
    execservice(domain, req_service) 

    """
    put_table(
        [
            ["Field", "Data"],
            ["domain", data['domain']],
            ["Service required", data['servicedata']]
        ]
    )"""
    
    """
    
    input("Input domain name", type=TEXT)
    checkbox("Services Required", options=['whois','traceroute'])
    
    """
    

if __name__ == '__main__':
    pywebio.start_server(reconserver, port=80)    