import whoisinfo
import pywebio
from pywebio.input import input, FLOAT, TEXT
from pywebio.output import put_text

def reconserver():
    #domain = input("give your domain name", type=TEXT)
    """
    text=whoisinfo.who(domain)
    put_text("your info: %s", text)
    """
    input.checkbox("Recon Options",options=['whois','nslookup','nmap'])

if __name__ == '__main__':
    pywebio.start_server(reconserver, port=80)