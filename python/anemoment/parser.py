from .models import WindData


class Parser:
    """
    Parses input from an Anemoment TriSonica.
    """

    def __init__(self, serial=None):
        """
        :param serial: A serial connection to continuously parse
        :type serial: serial.Serial
        """
        self.__serial = serial
        if self.__serial is not None and not self.__serial.is_open:
            self.__serial.open()

    def parse_string(self, data):
        """
        :param data: A line of Anemoment TriSonica formatted data
        :type data: string
        """
        pass



