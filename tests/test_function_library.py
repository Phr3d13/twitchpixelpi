import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import datetime

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import function_library

class TestFunctionLibrary(unittest.TestCase):
    
    @patch('function_library.Adafruit_NeoPixel')
    def setUp(self, mock_neopixel):
        self.mock_strip = mock_neopixel.return_value
        self.mock_strip.numPixels.return_value = 256  # Assuming 16x16 grid

    def test_SetAll(self):
        color = function_library.Color(255, 0, 0)  # Red
        function_library.SetAll(self.mock_strip, color)
        self.assertEqual(self.mock_strip.setPixelColor.call_count, 256)
        self.mock_strip.setPixelColor.assert_any_call(0, color)

    def test_FadeRGB(self):
        with patch('function_library.SetAll') as mock_set_all:
            function_library.FadeRGB(self.mock_strip)
            self.assertGreater(mock_set_all.call_count, 0)

    def test_Wheel(self):
        # Test red (0 degrees)
        self.assertEqual(function_library.Wheel(0), function_library.Color(0, 255, 0))
        # Test green (120 degrees)
        self.assertEqual(function_library.Wheel(85), function_library.Color(255, 0, 0))
        # Test blue (240 degrees)
        self.assertEqual(function_library.Wheel(170), function_library.Color(0, 0, 255))
        # Test a mixed color
        self.assertEqual(function_library.Wheel(42), function_library.Color(126, 129, 0))

    def test_Color(self):
        self.assertEqual(function_library.Color(255, 0, 0), 0xFF0000)
        self.assertEqual(function_library.Color(0, 255, 0), 0x00FF00)
        self.assertEqual(function_library.Color(0, 0, 255), 0x0000FF)

    def test_FadeInOut(self):
        with patch('function_library.SetAll') as mock_set_all:
            function_library.FadeInOut(self.mock_strip, 255, 0, 0)
            self.assertGreater(mock_set_all.call_count, 0)

    def test_Strobe(self):
        with patch('function_library.SetAll') as mock_set_all, \
             patch('time.sleep') as mock_sleep:
            function_library.Strobe(self.mock_strip, 255, 0, 0, 5, 0.5, 1)
            self.assertGreater(mock_set_all.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_Cylon(self):
        with patch('function_library.SetAll') as mock_set_all, \
             patch('time.sleep') as mock_sleep:
            function_library.Cylon(self.mock_strip, 255, 0, 0, 3, 0.1, 0.5)
            self.assertGreater(mock_set_all.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_Twinkle(self):
        with patch('time.sleep') as mock_sleep:
            function_library.Twinkle(self.mock_strip, 255, 0, 0, 8, 0.1, False)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_TwinkleRandom(self):
        with patch('time.sleep') as mock_sleep:
            function_library.TwinkleRandom(self.mock_strip, 8, 0.1, False)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_Sparkle(self):
        with patch('time.sleep') as mock_sleep:
            function_library.Sparkle(self.mock_strip, 255, 0, 0, 0.1)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_SnowSparkle(self):
        with patch('time.sleep') as mock_sleep:
            function_library.SnowSparkle(self.mock_strip, 255, 0, 0, 0.1, 0.1)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_RunningLights(self):
        with patch('time.sleep') as mock_sleep:
            function_library.RunningLights(self.mock_strip, 255, 0, 0, 0.1)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_ColorWipe(self):
        with patch('time.sleep') as mock_sleep:
            function_library.ColorWipe(self.mock_strip, 255, 0, 0, 0.1)
            self.assertEqual(self.mock_strip.setPixelColor.call_count, function_library.LED_COUNT)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_Rainbow(self):
        with patch('time.sleep') as mock_sleep:
            function_library.Rainbow(self.mock_strip, 20, 1)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_TheaterChase(self):
        with patch('time.sleep') as mock_sleep:
            function_library.TheaterChase(self.mock_strip, 255, 0, 0, 0.1, 10)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_TheaterChaseRainbow(self):
        with patch('time.sleep') as mock_sleep:
            function_library.TheaterChaseRainbow(self.mock_strip, 0.1)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_RunningLightsOther(self):
        with patch('time.sleep') as mock_sleep:
            function_library.RunningLightsOther(self.mock_strip, 255, 0, 0, 0.1)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_ColorWipeReverse(self):
        with patch('time.sleep') as mock_sleep:
            function_library.ColorWipeReverse(self.mock_strip, 255, 0, 0, 0.1)
            self.assertEqual(self.mock_strip.setPixelColor.call_count, function_library.LED_COUNT)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_RainbowCycle(self):
        with patch('time.sleep') as mock_sleep:
            function_library.RainbowCycle(self.mock_strip, 1, 0.1)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_RainbowCycleSlide(self):
        with patch('time.sleep') as mock_sleep:
            function_library.RainbowCycleSlide(self.mock_strip, 1, 0.1)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_ColorChase(self):
        with patch('time.sleep') as mock_sleep:
            function_library.ColorChase(self.mock_strip, 255, 0, 0, 0.1)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_ColorChaseReverse(self):
        with patch('time.sleep') as mock_sleep:
            function_library.ColorChaseReverse(self.mock_strip, 255, 0, 0, 0.1)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_MeteorRain(self):
        with patch('time.sleep') as mock_sleep, \
             patch('random.randint', return_value=6):
            # Mock the getPixelColor method to return a valid color value
            self.mock_strip.getPixelColor.return_value = function_library.Color(100, 100, 100)
            function_library.MeteorRain(self.mock_strip, 255, 0, 0, 10, 64, True, 0.1)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_NewKitt(self):
        with patch('time.sleep') as mock_sleep:
            function_library.NewKitt(self.mock_strip, 255, 0, 0, 8, 0.01, 0.05)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    @patch('function_library.Heat', [0] * function_library.LED_COUNT)
    def test_Fire(self):
        with patch('time.sleep') as mock_sleep, \
             patch('random.randint', return_value=6):
            function_library.Fire(self.mock_strip, function_library.Heat, 55, 120, 0.015)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    @patch('function_library.Freeze', [0] * function_library.LED_COUNT)
    def test_Ice(self):
        with patch('time.sleep') as mock_sleep, \
             patch('random.randint', return_value=6):
            function_library.Ice(self.mock_strip, function_library.Freeze, 55, 120, 0.015)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    @patch('function_library.Herb', [0] * function_library.LED_COUNT)
    def test_Safe(self):
        with patch('time.sleep') as mock_sleep, \
             patch('random.randint', return_value=6):
            function_library.Safe(self.mock_strip, function_library.Herb, 55, 120, 0.015)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_BouncingBalls(self):
        with patch('time.sleep') as mock_sleep, \
             patch('function_library.GetMillis', return_value=1000):
            function_library.BouncingBalls(self.mock_strip, 255, 0, 0, 3)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)

    def test_BouncingBallsRGB(self):
        with patch('time.sleep') as mock_sleep, \
             patch('function_library.GetMillis', return_value=1000):
            function_library.BouncingBallsRGB(self.mock_strip, 3, [[255,0,0],[0,255,0],[0,0,255]])
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)

    def test_HalloweenEyes(self):
        with patch('time.sleep') as mock_sleep, \
             patch('random.randint', return_value=6):
            function_library.HalloweenEyes(self.mock_strip, 255, 0, 0, 1, 1, True, 50, 0.1, 1)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_MorseCode(self):
        with patch('time.sleep') as mock_sleep:
            function_library.MorseCode(self.mock_strip, 255, 0, 0, "SOS", 0.1)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    @patch('function_library.datetime')
    def test_Clock1(self, mock_datetime):
        mock_datetime.now.return_value = datetime.datetime(2023, 1, 1, 12, 30, 45)
        function_library.Clock1(self.mock_strip)
        self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)

    @patch('datetime.datetime')
    def test_Clock2(self, mock_datetime):
        mock_datetime.now.return_value = datetime.datetime(2023, 1, 1, 12, 30, 45)
        function_library.Clock2(self.mock_strip, True)
        self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)

    def test_FillDownRandom(self):
        with patch('time.sleep') as mock_sleep, \
             patch('random.randint', return_value=128):
            function_library.FillDownRandom(self.mock_strip, 0, 0.1, 1, 0.2)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    # def test_RandomColors(self):
    #     with patch('time.sleep') as mock_sleep, \
    #         patch('random.randint', return_value=128):
    #         function_library.RandomColors(self.mock_strip, 0.1, iterations=3)
    #         self.assertEqual(self.mock_strip.setPixelColor.call_count, function_library.LED_COUNT * 3)
    #         self.assertEqual(mock_sleep.call_count, 3)

    def test_Blank(self):
        function_library.Blank(self.mock_strip)
        self.mock_strip.show.assert_called_once()

    def test_Cops(self):
        with patch('time.sleep') as mock_sleep:
            function_library.Cops(self.mock_strip, 5, 0.5, 3)
            self.assertGreater(self.mock_strip.setPixelColor.call_count, 0)
            self.assertGreater(mock_sleep.call_count, 0)

    def test_play(self):
        result = function_library.play("BombJack")
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()