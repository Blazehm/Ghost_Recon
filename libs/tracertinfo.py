import os

def tracert(self):
    command='tracert '+self
    process=os.popen(command)
    results=str(process.read())
    return results