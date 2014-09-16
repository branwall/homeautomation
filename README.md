homeautomation
==============
This is a library of scripts we're building to hopefully expand into a suite of home-automation tools.



At current, it contains only a basic weather API to be expanded into a weather-aware alarm clock.  There is also an email implementation being setup to receive commands and send out information.  

Combined, you should be able to email a pre-defined address the command "set my alarm for xx:xx XM" and receive an "okay" reply.  Then, at the preset time, we'll check the weather, find related music, and begin playing it at an increasing volume to wake you up.
===========
What you need:
Pythons 2 and 3
github (on pi by default)
pygame (on pi by default)
emacs  (sudo apt-get install emacs)
urllib2