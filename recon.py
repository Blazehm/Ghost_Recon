import libs.whoisinfo as whois
import libs.tracertinfo as trace
import pywebio
from pywebio.input import input, input_group, checkbox, FLOAT, TEXT
from pywebio.output import put_text, put_table

def reconserver():
    list=[]
    
    data= input_group(
        "Required Information",
        [
            input("Input domain name", name="domain", type=TEXT),
            checkbox("Services Required", name="servicedata",options=['whois','traceroute'])
        ]
    )

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