from django.test import TestCase
from unittest.mock import Mock, patch

from .parser import Parser


class TestParser(TestCase):
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