import whois

def who(self): #Function to return Whois Information
    w = whois.whois(self)
    return w
