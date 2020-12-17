#!/usr/bin/env python
import config
import utility
import socket
import time
import re
import main2
from function_library import *

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

try:
    s = socket.socket()
    s.connect((config.HOST, config.PORT))
    s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(config.NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(config.CHAN).encode("utf-8"))
    connected = True #Socket succefully connected
except Exception as e:
    print(str(e))
    connected = False #Socket failed to connect

def bot_loop():
    while connected:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            print("Pong")
        else:
            username = re.search(r"\w+", response).group(0) 
            message = CHAT_MSG.sub("", response)
            print(username + ": " + response)

            for pattern in config.COMMANDS:
                if re.match(pattern[0], message):
                    utility.chat(s, pattern[1])

            for pattern in config.NEO:
                if re.match(pattern[0], message):
                    main2.neo_loop1()

            for pattern in config.NEO2:
                if re.match(pattern[0], message):
                    main2.neo_loop2()

            for pattern in config.NEO3:
                if re.match(pattern[0], message):
                    main2.neo_loop3()

            for pattern in config.NEO4:
                if re.match(pattern[0], message):
                    main2.neo_loop4()

            for pattern in config.NEO5:
                if re.match(pattern[0], message):
                    main2.neo_loop5()

            for pattern in config.NEO6:
                if re.match(pattern[0], message):
                    main2.neo_loop6()

            for pattern in config.NEO7:
                if re.match(pattern[0], message):
                    main2.neo_loop7()
                    
            for pattern in config.NEO8:
                if re.match(pattern[0], message):
                    main2.neo_loop8()

            for pattern in config.NEO9:
                if re.match(pattern[0], message):
                    main2.neo_loop9()

            for pattern in config.MATRIX01:
                if re.match(pattern[0], message):
                    main2.neo_progmem_BombJack()

            for pattern in config.MATRIX02:
                if re.match(pattern[0], message):
                    main2.neo_progmem_Qbert()

            for pattern in config.MATRIX03:
                if re.match(pattern[0], message):
                    main2.neo_progmem_DigDug()

            for pattern in config.MATRIX04:
                if re.match(pattern[0], message):
                    main2.neo_progmem_Link()

            for pattern in config.BLANK:
                if re.match(pattern[0], message):
                    main2.blank()

            for pattern in config.BAN_PAT:
                if re.match(pattern, message):
                    utility.ban(s, username)
                    break
        time.sleep(1 / config.RATE)
if __name__ == "__main__":
    bot_loop()

