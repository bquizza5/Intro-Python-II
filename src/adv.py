from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("outside","Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("foyer","Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("overlook","Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("narrow","Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("treasure", "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_1 = Player('player1', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

running = True

while running == True:
    print('\nlocation: ',player_1.location.name)
    print('Description: ',player_1.location.description)

    action = input('\ntype action here: ').upper()

    if action == 'N':
        try:
            player_1.set_room(room[player_1.location.id].n_to)
        except AttributeError:
            print("\ncan't go that way...")

    elif action == 'E':
        try:
            player_1.set_room(room[player_1.location.id].e_to)
        except AttributeError:
            print("\ncan't go that way...")

    elif action == 'S':
        try:
            player_1.set_room(room[player_1.location.id].s_to)
        except AttributeError:
            print("\ncan't go that way...")

    elif action == 'W':
        try:
            player_1.set_room(room[player_1.location.id].w_to)
        except AttributeError:
            print("\ncan't go that way...")

    elif action == 'Q':
        running = False
    else: 
        print('\naction not valid\n')
        print('N = move north\nE = move east\nS = move south\nW = move west\nQ = quit')

