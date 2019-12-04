# Implement a class to hold room information. This should have name and
# description attributes.

class Room(object):
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description