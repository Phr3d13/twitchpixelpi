HOST = "irc.twitch.tv"              # This is Twitchs IRC server
PORT = 6667                         # Twitchs IRC server listens on port 6767
NICK = "phr3d13_bot"            # Twitch username your using for your bot
CHANNELS = ["#phr3d13", "#phr3d13_too"]                   # the channels you want the bot to join.
RATE = (20/30) # messages per seccond
BAN_PAT = [
    r"swear",
    r"some_pattern"
]
COMMANDS = [
#	[r"!discord", "the official discord: ____"],
	[r"!hibbidy", "Response"]
]

NEO = [
    [r"We have a NEW follower to the channel! Here's", "led"] # Message a bot says in your chat for new followers
]

NEO2 = [
    [r"We have a NEW Subscriber!", "led"],
    [r"^.* just subscribed for .* months in a row.*$", "led"],    # Message a bot says in your chat for re-subs
    [r"^.* just gifted .* a subscription.*$", "led"],    # Message a bot says in your chat for gifted subs
    [r"^.* just gifted .* subscriptions to random users in the channel.*$", "led"]    # Message a bot says in your chat for bulk gifted subs
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
    [r"!cops", "led"],
	[r"!oops", "led"]
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

NEO10 = [
    [r"!ice", "led"]
]

NEO11 = [
    [r"!kitt", "led"]
]

NEO12 = [
    [r"!safe", "led"]
]

NEO13 = [
    [r"!sparkle", "led"]
]

NEO14 = [
    [r"!zap", "led"]
]

NEO15 = [
    [r"!rainbow", "led"]
]

NEO16 = [
    [r"!pulse", "led"]
]

NEO17 = [
    [r"!heartbeat", "led"]
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
MATRIX06 = [
    [r"!kirby", "led"]
]
MATRIX07 = [
    [r"!frog", "led"]
]
MATRIX08 = [
    [r"!vinyl", "led"]
]
MATRIX09 = [
    [r"!heartbeat", "led"]
]