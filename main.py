#!/usr/bin/env python
import config
import utility
import socket
import time
import re
import main2
from secrets import secrets
from function_library import *

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

class IRCConn:
    def __init__(self, channel):
        try:
            self.sock = socket.socket()
            self.sock.settimeout(1.5) 
            self.sock.connect((config.HOST, config.PORT))
            self.sock.send("PASS {}\r\n".format(secrets.PASS).encode("utf-8"))
            self.sock.send("NICK {}\r\n".format(config.NICK).encode("utf-8"))
            self.sock.send("JOIN {}\r\n".format(channel).encode("utf-8"))
            self.connected = True #Socket succefully connected
        except Exception as e:
            print(str(e))
            self.connected = False #Socket failed to connect

def bot_loop():
    sockets = []
    for chan in config.CHANNELS:
        newsocket = IRCConn(chan)
        sockets.append(newsocket)
        if newsocket.connected is True:
            connected = True

    while connected:
        for irc in sockets:
            try:
                response = irc.sock.recv(1024).decode("utf-8")
            except Exception as e:
                print(str(e))
                response = ""
                continue
            if response == "PING :tmi.twitch.tv\r\n":
                irc.sock.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
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

                for pattern in config.NEO10:
                    if re.match(pattern[0], message):
                        main2.neo_loop10()

                for pattern in config.NEO11:
                    if re.match(pattern[0], message):
                        main2.neo_loop11()

                for pattern in config.NEO12:
                    if re.match(pattern[0], message):
                        main2.neo_loop12()

                for pattern in config.NEO13:
                    if re.match(pattern[0], message):
                        main2.neo_loop13()

                for pattern in config.NEO14:
                    if re.match(pattern[0], message):
                        main2.neo_loop14()

                for pattern in config.NEO15:
                    if re.match(pattern[0], message):
                        main2.neo_loop15()

                for pattern in config.NEO16:
                    if re.match(pattern[0], message):
                        main2.neo_loop16()

                for pattern in config.NEO17:
                    if re.match(pattern[0], message):
                        main2.neo_loop17()

                for pattern in config.MATRIX01:
                    if re.match(pattern[0], message):
                        main2.neo_progmem_run("BombJack")

                for pattern in config.MATRIX02:
                    if re.match(pattern[0], message):
                        main2.neo_progmem_run("Qbert")

                for pattern in config.MATRIX03:
                    if re.match(pattern[0], message):
                        main2.neo_progmem_run("DigDug")

                for pattern in config.MATRIX04:
                    if re.match(pattern[0], message):
                        main2.neo_progmem_run("Link",5,0.2)

                for pattern in config.MATRIX05:
                    if re.match(pattern[0], message):
                        main2.neo_progmem_run("Mario",20,0.1)

                for pattern in config.MATRIX06:
                    if re.match(pattern[0], message):
                        main2.neo_progmem_run("Kirby",5,0.1)
                        
                for pattern in config.MATRIX07:
                    if re.match(pattern[0], message):
                        main2.neo_progmem_run("Frog",5,0.1)
                        
                for pattern in config.MATRIX08:
                    if re.match(pattern[0], message):
                        main2.neo_progmem_run("Vinyl",5,0.1)
                        
                for pattern in config.MATRIX09:
                    if re.match(pattern[0], message):
                        main2.neo_progmem_run("Heartbeat",5,0.1)

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
