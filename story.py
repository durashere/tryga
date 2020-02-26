import os
import sys
import time
from player import player
from npcs import NPCS

screen_width = 80
#### Introduction ####


def speak(person, text):
    new_text = ''
    counter = 0
    if len(text) > screen_width:
        for char in text:
            new_text += char
            counter += 1
            if counter >= screen_width-10 and char == ' ':
                new_text += '\u2502'.rjust(screen_width-counter) + '\n\u2502 '
                counter = 0
        item = new_text
        item_end = '\u2502'.rjust(screen_width-counter)
    else:
        item = text
        item_end = '\u2502'

    print('\u250C' + '\u2500' * screen_width + '\u2510')
    print('\u2502 ' + person.capitalize().ljust(screen_width-1) + '\u2502')
    print('\u251C' + '\u2500' * screen_width + '\u2524')
    print('\u2502 ' + item.ljust(screen_width-1) + item_end)
    print('\u2514' + '\u2500' * screen_width + '\u2518')
    time.sleep(2)


def speak2(text):
    speech = text + '\n'
    for char in speech:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)


def setup_game():
    fisherman = NPCS['FISHERMAN'].name

    os.system('clear')

    #### Story intro ####

    speak('voice', 'You are sailing across the great ocean in searching for big treasure. When you are on the straight line to you goal, a storm suddenly arrives. The crew are asking you to turn back, but you are so close, that something inside telling you to ignore them. You decide to push forward and flow into the middle of the striking thunders!')

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

    os.system('clear')

    #### Name defining ####
    speak('stranger', 'Hello, you finally woke up. What should I call you?')
    player_name = input('\n > ')
    print()
    player.name = player_name.capitalize()
    speak('you', player.name + ', and you?')
    speak(fisherman, 'I\'m ' + fisherman + ', nice to meet you.')
    speak('you', 'Where I am? I can\'t remember anything!')
    speak(fisherman, 'You are in my fishing hut, as you can see I\'m a fisherman. I found you three day\'s ago on the beach and I took you there.')

    #### Profession defining ####
    speak(fisherman, player.name + ', what\'s your profession? You have three choices: [Warrior], [Mage] and [Ranger]')

    while True:
        player_job = input('\n > ')
        print()
        valid_jobs = ['warrior', 'mage']
        if player_job.lower() in valid_jobs:
            player.job = player_job
            speak(fisherman, 'You are now a ' + player_job + '!')
            break
        else:
            speak(fisherman, 'Unknown profession. Try again.')

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


setup_game()
