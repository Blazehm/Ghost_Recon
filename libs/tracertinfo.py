import os

def tracert(self): ##Function to return traceroute information
    command='tracert '+self
    process=os.popen(command)
    results=str(process.read())
    return results