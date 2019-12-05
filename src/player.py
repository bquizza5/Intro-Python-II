# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player(object):
    
    def __init__(self, name, location, items=None):
        self.name = name
        self.location = location
        self.items = [items]


    def set_room(self, room):
        self.location = room
    
    def pick_up_item(self, item):
        if self.items == [None]:
            self.items = [item]
        else:
            print('picked up', item.name)
            self.items.append(item)


    def drop_item(self,item):
        self.items.remove(item)
        print(item.name, 'dropped')
