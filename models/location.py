import json

class Location():
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def __repr__(self):
        return json.dumps(self.__dict__)
