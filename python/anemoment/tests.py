from django.test import TestCase
from unittest.mock import Mock, patch
from datetime import datetime, timedelta

from .parser import Parser
from .models import WindData


class TestModels(TestCase):
    def test_wind_data_timestamp_is_within_time(self):
        w = WindData()
        start_time = datetime.now() - timedelta(minutes=5)
        self.assertTrue(w.is_published_within(start_time))


class TestViews(TestCase):
    pass


class TestParser(TestCase):
    GOOD_ANEMOMENT_DATA = [
        {
            "raw_input": "05.2 112 -01.9 04.7 01.1 22.6",
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

    @patch("anemoment.parser.RawInputError")
    @patch("anemoment.parser.WindData")
    def test_parse_incomplete_anemoment_data(self, data_model, error_model):
        test_string = "52 41 -3"
        p = Parser()
        p.parse_string(test_string)
        error_model.objects.create.assert_called_with(type=error_model.E_INCOMPLETE, raw_input=test_string)
        data_model.objects.create.assert_not_called()

    @patch("anemoment.parser.RawInputError")
    @patch("anemoment.parser.WindData")
    def test_parse_invalid_anemoment_data(self, data_model, error_model):
        test_string = "34 -1 3 beef 2"
        p = Parser()
        p.parse_string(test_string)
        error_model.objects.create.assert_called_with(type=error_model.E_INVALID, raw_input=test_string)
        data_model.objects.create.assert_not_called()

