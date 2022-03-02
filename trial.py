from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI

res = DNSDumpsterAPI({'verbose':True}).search('google.com')
print(res)