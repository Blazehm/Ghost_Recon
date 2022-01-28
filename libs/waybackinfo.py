from waybackpy import WaybackMachineAvailabilityAPI

def wb(self):
    user_agent="Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
    availability_api = WaybackMachineAvailabilityAPI(self, user_agent)
    return availability_api.newest()


