import json

class Employee():
    def __init__(self, id, name, address, location_id):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id

    def __repr__(self):
        return json.dumps(self.__dict__)
