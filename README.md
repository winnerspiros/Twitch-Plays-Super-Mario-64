# Twitch-Plays-Super-Mario-64

This script is used with pc port but should work with emu too.
About pc port more info here can't help much more https://sm64pc.info/
This build requires python 3 in order to run.


# Installation
If you want to build yourself download python from https://www.python.org/downloads/ and run these in cmd:

• python -m pip install --upgrade pip
• pip install pyautogui
• pip install pynput
• pip install pydirectinput

else:

download the prebuilt pypy build I use here: https://mega.nz/file/PI1TUbYQ#kPtAjUUQJDcol5Yju4660EbvXoXerwM5KKhWi0sqwUM
extract in C:\
add new enviroment variable in path with the folder name e.x. C:\pypy
and done


# Keys

I have changes some keys like 'l' is jump and ',' is punch, 'b' is start.
In order to open cheats menu in pc port create a shortcut and put these at the end  '--skip-intro --cheats'.
Commands of the bot are posted here: https://justpaste.it/3923y 

# Run Script
Running is preety easy. Let's say you fixed the controls to match just go to TwitchPlays_AccountInfo.py put you stream username and oauth from here http://twitchapps.com/tmi/
Then run from a cmd/powershell 'python twitchplays.py' or if you got pypy type 'pypy3 twitchplays.py'. In case 'python twitchplays.py' doesnt work try 'python3', 'py', 'py3' or add variables cause they are missing.

About forever thing. It's a script that reruns the code in case of a crash. I think you need to npm install it, look here https://www.npmjs.com/package/forever
If you type forever on cmd and it returns stuff you are good to go. The file .bat should be self explained, the way it works is it runs and it hides, if you want to stop script check task manager for a node.js process.

# OBS Delay

First of all google how to enable low latency on twitch. Don't know why this is not default.
There are some ok tutorials on youtube how to reduce latency on obs. If you want to set a custom buffer check video stats while streaming for any setting that gives the lowest latency, else leave it on Auto.
Game is not that much time sensivite so all good.

# Fin
Bye
