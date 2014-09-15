#!/bin/bash

export PATH="/usr/lib/arm-linux-gnueabihf/libfm:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games"

if [ "$(( ( RANDOM % 40 ) + 1 ))" = "1" ]; then
	echo "Random Number == 1"
	/home/pi/dev/HomeAutomation/homeautomation/Weather/./bashPythonBridge.sh
fi
