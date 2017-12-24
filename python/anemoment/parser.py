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
        Assumes unit is configured to *NOT* show headers.
        :param data: A line of Anemoment TriSonica formatted data
        :type data: string
        """
        data = data.split(" ")
        data_len = len(data)
        new_value = {}
        if data_len != 5 and data_len != 6:
            # Throw/log an error here?
            return
        elif data_len == 5:
            new_value["temperature"] = 0
        else:
            new_value["temperature"] = float(data[5])
        new_value["speed"] = float(data[0])
        new_value["direction"] = float(data[1])
        new_value["north_south"] = float(data[2])
        new_value["west_east"] = float(data[3])
        new_value["up_down"] = float(data[4])
        WindData.objects.create(**new_value)



