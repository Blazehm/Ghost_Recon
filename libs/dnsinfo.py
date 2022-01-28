import dns 
import dns.resolver

def dnsresolveA(self):
    A_rec = dns.resolver.query(self,'A')
    resultA=''
    for exdata in A_rec:
        resultA=resultA+'A Record:'+exdata.to_text()+'\n'
    return resultA;

def dnsresolveMX(self):
    A_rec = dns.resolver.query(self,'MX')
    resultMX=''
    for exdata in A_rec:
        resultMX=resultMX+'MX Record:'+exdata.to_text()+'\n'
    return resultMX; 

