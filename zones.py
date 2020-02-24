import os
from player import player
screen_width = 80


class Zone:
    def __init__(self, name, subname, description, directions):
        self.name = name
        self.subname = subname
        self.description = description
        self.current = ' '
        self.directions = directions


def print_location():

    os.system('clear')

    ZONES[player.zone].current = 'x'
    current_zone_name = ZONES[player.zone].name
    current_zone_subname = ZONES[player.zone].subname
    current_zone_description = ZONES[player.zone].description

    print('\u250C' + '\u2500' * screen_width + '\u2510')
    print('\u2502' + ''.center(screen_width) + '\u2502')
    print('\u2502' + current_zone_name.center(screen_width) + '\u2502')
    print('\u2502' + current_zone_subname.center(screen_width) + '\u2502')
    print('\u2502' + ''.center(screen_width) + '\u2502')
    print('\u2502' + current_zone_description.center(screen_width) + '\u2502')

    print('\u2502' + ('\u250C' + ('\u2500' * (len(generate_map(minimap1)) - 2)) + '\u2510').center(screen_width) + '\u2502')
    print('\u2502' + generate_map(minimap1).center(screen_width) + '\u2502')
    print('\u2502' + generate_map(minimap2).center(screen_width) + '\u2502')
    print('\u2502' + generate_map(minimap3).center(screen_width) + '\u2502')
    print('\u2502' + generate_map(minimap4).center(screen_width) + '\u2502')
    print('\u2502' + generate_map(minimap5).center(screen_width) + '\u2502')
    print('\u2502' + ('\u2514' + ('\u2500' * (len(generate_map(minimap1)) - 2)) + '\u2518').center(screen_width) + '\u2502')

    print('\u2502' + ''.center(screen_width) + '\u2502')
    print('\u2514' + '\u2500' * screen_width + '\u2518')

########## Defining Zones ##########


ZONES = {}
ZONES['none'] = Zone('', '', '', {'up': ' ', 'right': '', 'down': ' ', 'left': ' '})
ZONES['TOWN_MARKET'] = Zone('Town', 'Market', 'The center of trade.',
                            {'up': ' ', 'right': ' ', 'down': ' ', 'left': 'TOWN_CASTLE'})
ZONES['TOWN_CASTLE'] = Zone('Town', 'Castle', 'The king place.',
                            {'up': ' ', 'right': 'TOWN_MARKET', 'down': ' ', 'left': ' '})


minimap1 = ['TOWN_CASTLE', 'TOWN_MARKET', 'none', 'none', 'none']
minimap2 = ['none', 'none', 'none', 'none', 'none']
minimap3 = ['none', 'none', 'none', 'none', 'none']
minimap4 = ['none', 'none', 'none', 'none', 'none']
minimap5 = ['none', 'none', 'none', 'none', 'none']


def generate_map(minimap):
    ZONES['none'].current = '\u2592'
    ZONES[player.zone].current = 'x'
    z1, z2, z3, z4, z5 = minimap

    def tile(zone):
        return '[' + ZONES[zone].current + ']'

    return '\u2502' + tile(z1) + tile(z2) + tile(z3) + tile(z4) + tile(z5) + '\u2502'
    # return '\u2502' + ZONES[z1].current + ZONES[z2].current + ZONES[z3].current + ZONES[z4].current + ZONES[z5].current + '\u2502'


def player_move(action):
    up = ZONES[player.zone].directions['up']
    right = ZONES[player.zone].directions['right']
    down = ZONES[player.zone].directions['down']
    left = ZONES[player.zone].directions['left']

    if action in ['up']:
        if up not in ['', ' ', 'none']:
            return move_handler(up)
    elif action in ['right']:
        if right not in ['', ' ', 'none']:
            return move_handler(right)
    elif action in ['down']:
        if down not in ['', ' ', 'none']:
            return move_handler(down)
    elif action in ['left']:
        if left not in ['', ' ', 'none']:
            return move_handler(left)
    print('\nYou can\'t go there.\n')


def move_handler(destination):
    ZONES[player.zone].current = ' '
    player.zone = destination
    ZONES[player.zone].current = 'x'
    print_location()
    print('You have moved to the ' + ZONES[player.zone].subname + '\n')


# Z_FOREST = Zone('Forest', 'The evil is hiding in darkness.')
'''
placeholder
{'up': ' ', 'right': ' ', 'down': ' ', 'left': ' '}


'''
