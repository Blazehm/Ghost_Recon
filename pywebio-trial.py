import libs.whoisinfo as whoisinfo
import libs.tracertinfo as trace
import pywebio
from pywebio.input import input, FLOAT, TEXT
from pywebio.output import put_text

def reconserver():
    domain = input("give your domain name", type=TEXT)
    """
    text=whoisinfo.who(domain)
    put_text("your info: %s", text)
    """
    t=trace.tracert(domain)
    put_text("TRACE: %s", t)
    print(t)

if __name__ == '__main__':
    pywebio.start_server(reconserver, port=80)