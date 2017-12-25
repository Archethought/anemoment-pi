from django.test import TestCase
from django.urls import reverse
from unittest.mock import Mock, patch
from datetime import timedelta
from django.utils import timezone

from .parser import Parser
from .models import WindData


def create_wind_data(
        minutes=0,
        speed=1,
        direction=14,
        north_south=13,
        west_east=12,
        up_down=-3.1,
        temperature=22):
    kwargs = {
        'speed': speed,
        'direction': direction,
        'north_south': north_south,
        'west_east': west_east,
        'up_down': up_down,
        'temperature': temperature,
    }
    timestamp = timezone.now() + timedelta(minutes=minutes)
    return WindData.objects.create(timestamp=timestamp, **kwargs)


class TestModels(TestCase):
    def test_wind_data_timestamp_is_within_time(self):
        create_time = timezone.now() - timedelta(minutes=2)
        w = WindData(timestamp=create_time)
        start_time = timezone.now() - timedelta(minutes=5)
        self.assertTrue(w.is_published_within(start_time))

    def test_wind_data_timestamp_is_not_within_time(self):
        create_time = timezone.now() - timedelta(minutes=5)
        w = WindData(timestamp=create_time)
        start_time = timezone.now() - timedelta(minutes=2)
        self.assertFalse(w.is_published_within(start_time))

        create_time = timezone.now() - timedelta(minutes=5)
        w = WindData(timestamp=create_time)
        start_time = timezone.now() - timedelta(minutes=15)
        end_time = timezone.now() - timedelta(minutes=10)
        self.assertFalse(w.is_published_within(start_time, end_time))


class TestViews(TestCase):
    def test_wind_data_no_data(self):
        response = self.client.get(reverse('wind_data'))
        j = response.json()
        self.assertEqual(len(j), 0)

    def test_wind_data_recent_is_pulled(self):
        data = create_wind_data()
        response = self.client.get(reverse('wind_data'))
        j = response.json()
        self.assertEqual(len(j), 1)
        self.assertEqual(j[0]['id'], data.id)

    def test_wind_data_old_is_not_pulled(self):
        create_wind_data(minutes=-10)
        start_time = timezone.now() - timedelta(minutes=5)
        response = self.client.get(reverse('wind_data')+"?start_time="+str(start_time))
        j = response.json()
        self.assertEqual(len(j), 0)


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

