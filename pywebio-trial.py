import libs.whoisinfo as whoisinfo
import libs.tracertinfo as trace
import pywebio
from pywebio.pin import put_input, pin
from pywebio.input import input, FLOAT, TEXT
from pywebio.output import put_text, put_buttons

def reconserver():
    put_input("domain_name", label="Put your domain name")
    """
    text=whoisinfo.who(domain)
    put_text("your info: %s", text)
    """
    put_buttons(['Get Pin Value'], lambda _: put_text(pin.domain_name))

    """t=trace.tracert(pin.domain_name)
    put_text("TRACE: %s", t)
    print(t)"""
    

if __name__ == '__main__':
    pywebio.start_server(reconserver, port=80)