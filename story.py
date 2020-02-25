import os
import sys
import time
from player import player

screen_width = 80
#### Introduction ####


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
