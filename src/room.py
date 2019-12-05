# Implement a class to hold room information. This should have name and
# description attributes.

class Room(object):
    def __init__(self, room_id, name, description, items=None):
        self.id = room_id
        self.name = name
        self.description = description
        self.items = [items]


    def add_item(self,item):
        if self.items == [None]:
            self.items = [item]
        else:
            self.items.append(item)


    def remove_item(self,item):
        self.items.remove(item)
