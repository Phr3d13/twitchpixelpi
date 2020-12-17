Simple Twitch IRC bot to control a NeoPixel strip with commands.


Setup assumes GPIO pin 12 will be used for a neopixel strip, and that your strip is 60 pixels (use function_library.py if you need to change number of leds or gpio pin). If using a 16x16 matrix of neopixels, setup assumes GPIO pin 13 will be used. LED GND and MATRIX GND must be brought to the Pi's GND pin to avoid garbage data.


Twitch bot code came from here: https://pimylifeup.com/raspberry-pi-twitch-bot/


Neopixel code came from here: https://github.com/BSFEMA/RPi_WS2812

If you run into this error when trying to run the bot:
```
ImportError: No module named _rpi_ws281x
```
Do this:
```
sudo pip install rpi_ws281x
```


config.py needs to be edited as follows:

```
HOST = "irc.twitch.tv"              # This is Twitchs IRC server
PORT = 6667                         # Twitchs IRC server listens on port 6767
NICK = "twitch_username"            # Twitch username your using for your bot
PASS = "your_oauthtoken" # your Twitch OAuth token
CHAN = "#your_channel"                   # the channel you want the bot to join.
```
NICK is the twitch username the bot would be using (all letters in lowercase).  

PASS is the oauth token for the twitch account the bot would be using. Sign into a web browser with the bot's account,  
    and go here: https://twitchapps.com/tmi/ you need the whole oauth including the "oauth:"  

CHAN is the Twitch streamer account you want the bot to read and respond to (again, all letters in lowercase).  


To run the bot:
```
sudo python3 main.py
```

To run the bot as a service, and set it to start automatically at boot:

Create a new file for the service:
```
sudo nano /etc/systemd/system/twitchbot.service
```
Copy /Paste this code chunk into it:
```
[Unit]
Description=twitch bot
After=network.target
StartLimitIntervalSec=0
[Service]
Type=simple
Restart=always
RestartSec=1
ExecStart=python3 /home/pi/twitchpixelpi/main.py

[Install]
WantedBy=multi-user.target
```
Ctrl+O to write out the file (save) then Ctrl+X to exit nano.


To start the service:
```
sudo service twitchbot start
```
To stop the service:
```
sudo service twitchbot stop
```
To make the service start at boot:
```
sudo systemctl enable twitchbot
```
