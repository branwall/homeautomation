#!/usr/bin/python

#uses Python2.7

import os, pygame, sys

from random import randrange

#GRAB current weather through bash from GetWeather.py using temp file
currentWeather = ""
for i in sys.argv[1:]:
    if (i!=sys.argv[len(sys.argv)-1]):
        currentWeather+= i + " ";
    else:
        currentWeather+= i;

# hold the current weather category from python sctipt directly (FAILED DUE TO VERSION COLLISION)
#currentWeather = GetWeather.weatherReturn();

#choose correct directory 
#   os.chdir('D:/weathersounds/' + currentWeather + '/Ambient/');
#     "/media/MUH BABY/WeatherSounds"
#change to your directory

os.chdir('/media/MUH BABY/WeatherSounds/' + currentWeather + '/Environmental');
path = os.getcwd();

#store a list of all the files
# !! note assumes only music files in folder, no sub directories or excess!!
SoundsList = os.listdir(path);

#choose file to play
sound= SoundsList[randrange(0,len(SoundsList))];


#AUDIO PLAYER PORTION
pygame.mixer.init()
pygame.mixer.music.load(sound) #replace help.mp3 with 'sound' variable
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    continue
