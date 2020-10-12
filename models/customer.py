import json

class Customer():
    def __init__(self, id, name, business, locationId):
        self.id = id
        self.name = name
        self.business = business
        self.locationId = locationId

    def __repr__(self):
        return json.dumps(self.__dict__)
