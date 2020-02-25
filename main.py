
# Python Text RPG Game
# TryGa

##### Imports #####
import cmd
import textwrap
import sys
import os
import time
import random
##### Self imports #####
from player import player
import zones
from zones import ZONES
import story

##### Settings #####
screen_width = 80

########## Title Screen ##########


def title_screen_choices():
    option = input(' > ')
    if (option == '1'):
        story.setup_game()
    elif (option == '2'):
        print('2')
    elif (option == '3'):
        sys.exit()
    while option not in ['1', '2', '3']:
        print('Choice not valid.')


def title_screen():
    os.system('clear')
    print('\u250C' + '\u2500' * screen_width + '\u2510')
    print('\u2502' + ''.center(screen_width) + '\u2502')
    print('\u2502' + r' _____             _____        '.center(screen_width) + '\u2502')
    print('\u2502' + r'|_   _|           |  __ \       '.center(screen_width) + '\u2502')
    print('\u2502' + r'  | | _ __  _   _ | |  \/  __ _ '.center(screen_width) + '\u2502')
    print('\u2502' + r"  | || '__|| | | || | __  / _` |".center(screen_width) + '\u2502')
    print('\u2502' + r'  | || |   | |_| || |_\ \| (_| |'.center(screen_width) + '\u2502')
    print('\u2502' + r'  \_/|_|    \__, | \____/ \__,_|'.center(screen_width) + '\u2502')
    print('\u2502' + r'             __/ |              '.center(screen_width) + '\u2502')
    print('\u2502' + r'            |___/               '.center(screen_width) + '\u2502')
    print('\u2502' + ''.center(screen_width) + '\u2502')
    print('\u2502' + ''.center(screen_width) + '\u2502')
    print('\u2502' + 'Copyright by Duras'.center(screen_width) + '\u2502')
    print('\u2502' + ''.center(screen_width) + '\u2502')
    print('\u2514' + '\u2500' * screen_width + '\u2518')
    time.sleep(1)

    os.system('clear')
    print('\u250C' + '\u2500' * screen_width + '\u2510')
    print('\u2502' + ''.center(screen_width) + '\u2502')
    print('\u2502' + '[1] Start'.center(screen_width) + '\u2502')
    print('\u2502' + '[2] Load'.center(screen_width) + '\u2502')
    print('\u2502' + '[3] Quit'.center(screen_width) + '\u2502')
    print('\u2502' + ''.center(screen_width) + '\u2502')
    print('\u2514' + '\u2500' * screen_width + '\u2518')


########## Game Interactivity ##########
def prompt():
    print('What you want to do?')
    action = input(' > ').split(' ')

    if action[0].lower() in ['quit', 'exit']:
        if len(action) == 1:
            sys.exit()
            return
    elif action[0].lower() in ['move']:
        if 3 > len(action) > 1:
            return zones.player_move(action[1])
        else:
            return print('Specify in what direction you want to go.')
    elif action[0].lower() in ['map']:
        if len(action) == 1:
            zones.print_location()
            print('You are in ' + zones.ZONES[player.zone].subname + '\n')
            return
    elif action[0].lower() in ['examine']:
        if len(action) == 1:
            player_examine(action[0])
            return
    print('\nUnknown action, try again.\n')


def player_examine(action):
    print('examine')


########## Game Funcionality ##########


########## Game Loop ##########

def main_game_loop():
    while player.game_over == False:
        prompt()


# title_screen()
# title_screen_choices()
# main_game_loop()
story.setup_game()
