from django.apps import AppConfig
import serial

class AnemomentConfig(AppConfig):
    name = 'anemoment'
    perser = None

    def ready(self):
        """
        Runs on application startup.
        """
        UART = None
        from .parser import Parser

        if UART is not None:
            ser = serial.Serial(port=UART, baudrate=115200)
        else:
            ser = None
        self.parser = Parser(ser)
