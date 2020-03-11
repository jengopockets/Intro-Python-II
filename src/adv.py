from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
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
while True:
    cmd = input("What is your name adventurer? \n")
    player = Player(cmd,room['outside'])
    print(player)
    break

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
while True:
    cmd = input("->")
    current_room = player.current_room

    if cmd == "q":
        print("Goodbye scardy cat!")
        break
    elif cmd == "n":
        if current_room.n_to == None:
            print(f'You hit a wall {player.name}')
        else:
            player.current_room = current_room.n_to
            print("You move North")
            print(current_room.n_to)
    elif cmd == "s":
        if current_room.s_to == None:
            print(f'You hit a wall {player.name}')
        else:
            player.current_room = current_room.s_to
            print("You move South")
            print(current_room.s_to)
    elif cmd == "e":
        if current_room.e_to == None:
            print(f'You hit a wall {player.name}')
        else:
            player.current_room = current_room.e_to
            print("You move East")
            print(current_room.e_to)
    elif cmd == "w":
        if current_room.w_to == None:
            print(f'You hit a wall {player.name}')
        else:
            player.current_room = current_room.w_to
            print("You move West")
            print(current_room.w_to)
    else:
        print("ERROR: Valid Commands are n for north, s for south, e for east, w for west, or q for quit")
    
