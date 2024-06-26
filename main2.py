#This is the main.  This meeds to import function_library.py in order to work.

#Import the 'functions_library' which animates the LEDs in various ways.
from function_library import *
import time

#Main program logic:




if __name__ == '__main2__':
        #Process arguments
        opt_parse()
        #Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        #Intialize the library (must be called once before other functions).
        strip.begin()

        print ('Press Ctrl-C to quit.')

def neo_loop1():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  Cylon(strip, 255, 0, 0, 3, .1, .5)")
    for i in range (5):
        Cylon(strip, (random.randrange(0, 255)), (random.randrange(0, 255)), (random.randrange(0, 255)), 7, .05, .01)

def neo_loop2():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  TheaterChaseRainbow(strip, .1)")
    TheaterChaseRainbow(strip, .1)

def blank():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    #strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    strip = Adafruit_NeoPixel(MATRIX_COUNT, MATRIX_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, MATRIX_BRIGHTNESS, MATRIX_CHANNEL, LED_STRIP)
	#Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  Blank(strip)")
    Blank(strip)

def neo_loop3():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #Intialize the library (must be called once before other functions).
    strip.begin()
    t_end = time.time() + 60 * 1
    print("Calling:  Strobe(strip, 255, 255, 255, 5, .25, 3)")
    Strobe(strip, 200, 200, 200, 20, .15, 3)
    print("Calling:  Blank(strip)")
    Blank(strip)

def neo_loop4():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  RunningLights(strip, 255, 255, 255, .25)")
    RunningLights(strip, (random.randrange(0, 125, 15)), (random.randrange(0, 125, 15)), (random.randrange(0, 125, 15)), .1)
    Blank(strip)

def neo_loop5():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #strip = Adafruit_NeoPixel(MATRIX_COUNT, MATRIX_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, MATRIX_CHANNEL, LED_STRIP)
	#Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  Cops(strip, 5, .5, 3)")
    Cops(strip, 5, .5, 3)
    Blank(strip)

def neo_loop6():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #strip = Adafruit_NeoPixel(MATRIX_COUNT, MATRIX_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, MATRIX_CHANNEL, LED_STRIP)
	#Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  Fire(strip, Heat, 75, 150, .015) #This looks a lot better looped...")
    for i in range (300):
        Fire(strip, Heat, 75, 150, .015)
    Blank(strip)

def neo_loop7():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  MorseCode(strip, 255, 255, 255, 'SOS. This is a test.', .15)")
    MorseCode(strip, 255, 255, 255, 'Phr3d13', .15)
    Blank(strip)

def neo_loop8():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  SnowSparkle(strip, 10, 10, 10, .1, random.uniform(0, .5))")
    for i in range (30):
        SnowSparkle(strip, 10, 10, 10, .1, random.uniform(0, .5))
    Blank(strip)

def neo_loop9():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #strip = Adafruit_NeoPixel(MATRIX_COUNT, MATRIX_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, MATRIX_CHANNEL, LED_STRIP)
    #Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  NewKitt(strip, 255, 0, 0, 8, .01, .05)")
    NewKitt(strip, random.randint(0, 150), random.randint(0, 150), random.randint(0, 150), 8, .1, .1)
    Blank(strip)

def neo_loop10():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #strip = Adafruit_NeoPixel(MATRIX_COUNT, MATRIX_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, MATRIX_CHANNEL, LED_STRIP)
	#Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  Ice(strip, Freeze, 75, 150, .015) #This looks a lot better looped...")
    for i in range (300):
        Ice(strip, Freeze, 75, 150, .015)
    Blank(strip)

def neo_loop11():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #strip = Adafruit_NeoPixel(MATRIX_COUNT, MATRIX_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, MATRIX_CHANNEL, LED_STRIP)
    #Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  NewKitt(strip, 255, 0, 0, 8, .01, .05)")
    for i in range (5):
        Cylon(strip, random.randint(0, 150), random.randint(0, 150), random.randint(0, 150), 8, .05, .05)
    Blank(strip)

def neo_loop12():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #strip = Adafruit_NeoPixel(MATRIX_COUNT, MATRIX_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, MATRIX_CHANNEL, LED_STRIP)
	#Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  Ice(strip, Freeze, 75, 150, .015) #This looks a lot better looped...")
    for i in range (300):
        Safe(strip, Herb, 75, 150, .015)
    Blank(strip)

def neo_loop13():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #strip = Adafruit_NeoPixel(MATRIX_COUNT, MATRIX_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, MATRIX_CHANNEL, LED_STRIP)
	#Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  Sparkle(strip, red, green, blue, SpeedDelay) #This looks a lot better looped...")
    for i in range (300):
        Sparkle(strip, 127, 0, 150, .015)
    Blank(strip)

def neo_loop14():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #strip = Adafruit_NeoPixel(MATRIX_COUNT, MATRIX_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, MATRIX_CHANNEL, LED_STRIP)
	#Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  Sparkle(strip, red, green, blue, SpeedDelay) #This looks a lot better looped...")
    for i in range (300):
        Sparkle(strip, 127, 127, 0, .015)
    Blank(strip)

def neo_loop15():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #strip = Adafruit_NeoPixel(MATRIX_COUNT, MATRIX_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, MATRIX_CHANNEL, LED_STRIP)
	#Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  Rainbow(strip, SpeedDelay) ")
    #for i in range (200):
    Rainbow(strip, 5)
    Blank(strip)

def neo_loop16():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #strip = Adafruit_NeoPixel(MATRIX_COUNT, MATRIX_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, MATRIX_CHANNEL, LED_STRIP)
	#Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  FadeInOut(strip, red, green, blue) #This looks a lot better looped...")
    for i in range (10):
        FadeInOut(strip, 0, 255, 0)
    Blank(strip)

def neo_loop17():
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #strip = Adafruit_NeoPixel(MATRIX_COUNT, MATRIX_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, MATRIX_CHANNEL, LED_STRIP)
	#Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  Heartbeat(strip, red, green, blue, fade_in_speed, fade_out_speed) ")
    for i in range (6):    
        Heartbeat(strip, 255, 0, 0, 0.0001, 0.0001)
        Heartbeat(strip, 255, 0, 0, 0.0001, 0.0001)
        time.sleep(0.2)
    Blank(strip)


def neo_progmem_run(GameName, loops=3, sleep=0.5):
    #Process arguments
    opt_parse()
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(MATRIX_COUNT, MATRIX_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, MATRIX_BRIGHTNESS, MATRIX_CHANNEL, LED_STRIP)
    #Intialize the library (must be called once before other functions).
    strip.begin()
    print("Calling:  CharAnimation(",GameName,",",loops,", ",sleep,")")
    CharAnimation(strip, GameName, loops, sleep)
    Blank(strip)

"""
while True:
            print("Calling:  FadeRGB(strip)")
            FadeRGB(strip)
            print("Calling:  FadeInOut(strip, 255, 255, 255)")
            FadeInOut(strip, 255, 255, 255)
            print("Calling:  Strobe(strip, 255, 255, 255, 5, .5, 3)")
            Strobe(strip, 255, 255, 255, 5, .5, 3)
            print("Calling:  Cylon(strip, 255, 0, 0, 3, .1, .5)")
            Cylon(strip, 255, 0, 0, 3, .1, .5)
            print("Calling:  Twinkle(strip, 255, 0, 0, 8, .1, False)")
            Twinkle(strip, 255, 0, 0, 8, .1, False)
            print("Calling:  TwinkleRandom(strip, 8, .1, False)")
            TwinkleRandom(strip, 8, .1, False)
            print("Calling:  Sparkle(strip, 255, 255, 255, 0)")
            Sparkle(strip, 255, 255, 255, 0)
            print("Calling:  SnowSparkle(strip, 10, 10, 10, .1, random.uniform(0, .5))")
            SnowSparkle(strip, 10, 10, 10, .1, random.uniform(0, .5))
            print("Calling:  RunningLights(strip, 255, 255, 255, .25)")
            RunningLights(strip, 255, 255, 255, .25)
            print("Calling:  ColorWipe(strip, 255, 0, 0, .02)")
            ColorWipe(strip, 255, 0, 0, .02)
            print("Calling:  ColorWipeReverse(strip, 0, 255, 0, .02)")
            ColorWipeReverse(strip, 0, 255, 0, .02)
            print("Calling:  Rainbow(strip, 0)")
            Rainbow(strip, 0)
            print("Calling:  RainbowCycle(strip, 5, 0)")
            RainbowCycle(strip, 5, 0)
            print("Calling:  ColorChase(strip, 0, 0, 255, .02)")
            ColorChase(strip, 0, 0, 255, .02)
            print("Calling:  ColorChaseReverse(strip, 0, 255, 0, .02)")
            ColorChaseReverse(strip, 0, 255, 0, .02)
            print("Calling:  TheaterChase(strip, 255, 0, 0, .2, 10)")
            TheaterChase(strip, 255, 0, 0, .2, 10)
            print("Calling:  TheaterChaseRainbow(strip, .1)")
            TheaterChaseRainbow(strip, .1)
            print("Calling:  MeteorRain(strip, 255, 0, 0, 5, 64, True, .1)")
            MeteorRain(strip, 255, 0, 0, 5, 64, True, .1)
            print("Calling:  NewKitt(strip, 255, 0, 0, 8, .01, .05)")
            NewKitt(strip, 255, 0, 0, 8, .01, .05)
            print("Calling:  Fire(strip, Heat, 75, 150, .015) #This looks a lot better looped...")
            Fire(strip, Heat, 75, 150, .015) #This looks a lot better looped...
            print("Calling:  BouncingBalls(strip, 255, 0, 0, 3)")
            BouncingBalls(strip, 255, 0, 0, 3)
            print("Calling:  BouncingBallsRGB(strip, 3, [[255, 0, 0], [0, 255, 0], [0, 0, 255]])")
            BouncingBallsRGB(strip, 3, [[255, 0, 0], [0, 255, 0], [0, 0, 255]])
            print("Calling:  HalloweenEyes(strip, 255, 0, 0, 1, 4, True, random.randint(5, 50), random.uniform(.01, .2), random.randrange(1, 3))")
            HalloweenEyes(strip, 255, 0, 0, 1, 4, True, random.randint(5, 50), random.uniform(.01, .2), random.randrange(1, 3))
            print("Calling:  MorseCode(strip, 255, 255, 255, 'SOS. This is a test.', .15)")
            MorseCode(strip, 255, 255, 255, 'SOS. This is a test.', .15)
            print("Calling:  Clock1(strip)")
            Clock1(strip)
            print("Calling:  Clock2(strip, True)")
            Clock2(strip, True)
            print("Calling:  FillDownRandom(strip, 0, .1, 1, .2)")
            FillDownRandom(strip, 0, .1, 1, .2)
            print("Calling:  RandomColors(strip, .1)")
            RandomColors(strip, .1)
            print("========================================")
            print("Looping")
            print("========================================")

#List of functions:
		FadeRGB(strip)
		FadeInOut(strip, 255, 255, 255)
		Strobe(strip, 255, 255, 255, 5, .5, 3)
		Cylon(strip, 255, 0, 0, 3, .1, .5)
		Twinkle(strip, 255, 0, 0, 8, .1, False)
		TwinkleRandom(strip, 8, .1, False)
		Sparkle(strip, 255, 255, 255, 0)
		SnowSparkle(strip, 10, 10, 10, .1, random.uniform(0, .5))
		RunningLights(strip, 255, 255, 255, .25)
		ColorWipe(strip, 255, 0, 0, .02)
		ColorWipeReverse(strip, 0, 255, 0, .02)
		Rainbow(strip, 0)
		RainbowCycle(strip, 5, 0)
		ColorChase(strip, 0, 0, 255, .02)
		ColorChaseReverse(strip, 0, 255, 0, .02)
		TheaterChase(strip, 255, 0, 0, .2, 10)
		TheaterChaseRainbow(strip, .1)
		MeteorRain(strip, 255, 0, 0, 5, 64, True, .1)
		NewKitt(strip, 255, 0, 0, 8, .01, .05)
		Fire(strip, Heat, 75, 150, .015)
		BouncingBalls(strip, 255, 0, 0, 3)
		BouncingBallsRGB(strip, 3, [[255, 0, 0], [0, 255, 0], [0, 0, 255]])
		HalloweenEyes(strip, 255, 0, 0, 1, 4, True, random.randint(5, 50), random.uniform(.01, .2), random.randrange(1, 3))
		MorseCode(strip, 255, 255, 255, 'SOS. This is a test.', .15)
		Clock1(strip)
		Clock2(strip, True)
		FillDownRandom(strip, 0, .1, 1, .2)
		RandomColors(strip, .1)
"""
