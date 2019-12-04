# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player(object):
    
    def __init__(self, name, location):
        self.name = name
        self.location = location


    def set_room(self, room):
        self.location = room
