from django.apps import AppConfig
import serial

class AnemomentConfig(AppConfig):
    name = 'anemoment'

    def ready(self):
        """
        Runs on application startup.
        """
        # UART = None
        UART = "/dev/ttyAMA0"
        from .parser import Parser
        print(UART)
        if UART is not None:
            ser = serial.Serial(port=UART, baudrate=115200)
        else:
            ser = None
        self.parser = Parser(ser)
