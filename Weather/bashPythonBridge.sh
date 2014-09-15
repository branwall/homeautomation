#!/bin/bash

python3 /home/pi/dev/HomeAutomation/homeautomation/Weather/GetWeather.py > tempfile.txt
var=`cat tempfile.txt`
rm tempfile.txt

python /home/pi/dev/HomeAutomation/homeautomation/Weather/WeatherAudio.py $var