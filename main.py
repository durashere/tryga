
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

##### Settings #####
screen_width = 80

########## Title Screen ##########


def title_screen_choices():
    option = input(' > ')
    if (option == '1'):
        setup_game()
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

def setup_game():
    os.system('clear')

    def speak(person, text):
        speech = '[' + person.capitalize() + ']: ' + text + '\n\n'
        for char in speech:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.02)

    def speak2(text):
        speech = text + '\n'
        for char in speech:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.001)

    #### Story intro ####

    speak('voice', 'You are sailing across the great ocean in searching for big treasure.\n\
         When you are on the straight line to you goal, a storm suddenly arrives.\n\
         The crew are asking you to turn back, but you are so close, that something inside telling you to ignore them.\n\
         You decide to push forward and flow into the middle of the striking thunders!')
    time.sleep(1)
    speak('voice', 'Clouds and darkness surround you...')

    os.system('clear')

    speak2('' + r' _____             _____        '.center(screen_width) + '')
    speak2('' + r'|_   _|           |  __ \       '.center(screen_width) + '')
    speak2('' + r'  | | _ __  _   _ | |  \/  __ _ '.center(screen_width) + '')
    speak2('' + r"  | || '__|| | | || | __  / _` |".center(screen_width) + '')
    speak2('' + r'  | || |   | |_| || |_\ \| (_| |'.center(screen_width) + '')
    speak2('' + r'  \_/|_|    \__, | \____/ \__,_|'.center(screen_width) + '')
    speak2('' + r'             __/ |              '.center(screen_width) + '')
    speak2('' + r'            |___/               '.center(screen_width) + '\n')

    time.sleep(3)

    #### Name defining ####
    speak('stranger', 'Hello, you finally woke up. What should I call you?')
    player_name = input(' > ')
    player.name = player_name.capitalize()
    print()
    speak('you', player.name + ', and you?')
    speak('NPC1', 'I\'m NPC1, nice to meet you.')
    speak('you', 'Where I am? I can\'t remember anything!')
    speak('NPC1', 'You are in my fishing hut, as you can see I\'m a fisherman.\n\
        I found you three day\'s ago on the beach and I took you there.')

    #### Profession defining ####
    speak('stranger', player.name + ', what\'s your profession?\n\
            You have three choices:\n\
            - Warrior\n\
            - Mage\n\
            - Ranger')

    while True:
        player_job = input('\n > ')
        valid_jobs = ['warrior', 'mage']
        if player_job.lower() in valid_jobs:
            player.job = player_job
            speak('stranger', 'You are now a ' + player_job + '!\n')
            break
        else:
            speak('stranger', '\n Unknown profession.\nTry again.\n')

    #### Stats defining ####
    if player.job == 'warrior':
        player.hp = 120
        player.mp = 20
    elif player.job == 'mage':
        player.hp = 60
        player.mp = 100

    print(player.job)
    print(player.hp)
    print(player.mp)


########## Game Loop ##########

def main_game_loop():
    while player.game_over == False:
        prompt()


# title_screen()
# title_screen_choices()
# main_game_loop()
# setup_game()
