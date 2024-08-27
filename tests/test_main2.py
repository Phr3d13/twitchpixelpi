import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import main2
# import function_library

class TestMain2(unittest.TestCase):

    @patch('main2.Adafruit_NeoPixel')
    @patch('main2.opt_parse')  # Mock the opt_parse function
    # @patch('main2.parse_args')
    def setUp(self, mock_opt_parse, mock_neopixel): #, mock_parse_args):
        self.mock_strip = mock_neopixel.return_value
        self.mock_strip.numPixels.return_value = 256  # Assuming 16x16 grid
        # Make opt_parse return a mock object that doesn't do anything
        mock_opt_parse.return_value = MagicMock()
        # mock_parse_args.return_valuse = MagicMock()

    @patch('main2.Cylon')
    def test_neo_loop1(self, mock_cylon):
        main2.neo_loop1()
        self.assertEqual(mock_cylon.call_count, 5)
        mock_cylon.assert_called_with(self.mock_strip, 
                                      unittest.mock.ANY,  # random color
                                      unittest.mock.ANY,  # random color
                                      unittest.mock.ANY,  # random color
                                      7, .05, .01)

    @patch('main2.TheaterChaseRainbow')
    def test_neo_loop2(self, mock_theater):
        main2.neo_loop2()
        mock_theater.assert_called_once_with(self.mock_strip, .1)

    @patch('main2.Blank')
    def test_blank(self, mock_blank):
        main2.blank()
        mock_blank.assert_called_once_with(self.mock_strip)

if __name__ == '__main__':
    unittest.main()
