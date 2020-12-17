HOST = "irc.twitch.tv"              # This is Twitchs IRC server
PORT = 6667                         # Twitchs IRC server listens on port 6767
NICK = "twitch_username"            # Twitch username your using for your bot
PASS = "your_oauthtoken" # your Twitch OAuth token
CHAN = "#your_channel"                   # the channel you want the bot to join.
RATE = (20/30) # messages per seccond
BAN_PAT = [
    r"swear",
    r"some_pattern"
]
COMMANDS = [
	[r"!discord", "the official discord: ____"],
	[r"!hibbidy", "Response"]
]

NEO = [
    [r"your_bot_message", "led"] # Message a bot says in your chat for new followers
# If you a follow/re-follow message that uses the user name at the beginning of the message
# you can uncomment the next line and edit as necessary   
#    [r"^.* just followed .*$", "led"]    # Message a bot says in your chat for re-subs
]

NEO2 = [
    [r"your_bot_message", "led"] # Message a bot says in your chat for new subscribers
# If you a sub/re-sub message that uses the user name at the beginning of the message
# you can uncomment the next line and edit as necessary   
#    [r"^.* just subscribed for .*$", "led"]    # Message a bot says in your chat for re-subs
]

BLANK = [
    [r"!blank", "led"]
]

NEO3 = [
    [r"!strobe", "led"]
]

NEO4 = [
    [r"!party", "led"]
]

NEO5 = [
    [r"!cops", "led"]
]

NEO6 = [
    [r"!fire", "led"]
]

NEO7 = [
    [r"!morse", "led"]
]

NEO8 = [
    [r"Thank you very much .* for the tip of .*$", "led"]
]

NEO9 = [
    [r"!newkitt", "led"]
]

MATRIX01 = [
    [r"!bombjack", "led"]
]

MATRIX02 = [
    [r"!qbert", "led"]
]

MATRIX03 = [
    [r"!digdug", "led"]
]
MATRIX04 = [
    [r"!link", "led"]
]
MATRIX05 = [
    [r"!mario", "led"]
]