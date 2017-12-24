from django.test import TestCase
from unittest.mock import Mock, patch

from .parser import Parser


class TestParser(TestCase):
    GOOD_ANEMOMENT_DATA = [
        {
            "raw_input": "S 05.2 D 112 U -01.9 V 04.7 W 01.1 T 22.6",
            "parsed_data": {
                "speed": 5.2,
                "direction": 112,
                "north_south": -1.9,
                "west_east": 4.7,
                "up_down": 1.1,
                "temperature": 22.6,
            }
        },
    ]

    def setUp(self):
        self.mock_serial = Mock()

    def test_starts_serial_port_if_not_open(self):
        self.mock_serial.is_open = False
        Parser(self.mock_serial)
        self.mock_serial.open.assert_called_once()

    def test_does_not_start_serial_port_if_open(self):
        self.mock_serial.is_open = True
        Parser(self.mock_serial)
        self.mock_serial.open.assert_not_called()

    @patch("anemoment.parser.WindData")
    def test_parse_good_anemoment_data(self, model):
        p = Parser()
        for e in self.GOOD_ANEMOMENT_DATA:
            p.parse_string(e["raw_input"])
            model.objects.create.assert_called_with(**e["parsed_data"])
