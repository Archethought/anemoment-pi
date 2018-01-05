from .models import WindData, RawInputError
from threading import Thread


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
        if self.__serial is not None:
            if not self.__serial.is_open:
                self.__serial.open()
            self.t = Thread(target=self.__worker)
            self.t.start()

    def __worker(self):
        while 1:
            self.parse_string(str(self.__serial.readline())[3:-6])

    def parse_string(self, input_data):
        """
        Assumes unit is configured to *NOT* show headers.
        :param input_data: A line of Anemoment TriSonica formatted data
        :type input_data: string
        """
        data = input_data.split(" ")
        data = list(filter(None, data))
        data_len = len(data)
        new_value = {}
        if data_len < 5:
            RawInputError.objects.create(type=RawInputError.E_INCOMPLETE, raw_input=input_data)
            return
        elif data_len == 5:
            new_value["temperature"] = 0
        else:
            new_value["temperature"] = data[5]
        try:
            new_value["temperature"] = float(new_value["temperature"])
            new_value["speed"] = float(data[0])
            new_value["direction"] = float(data[1])
            new_value["north_south"] = float(data[2])
            new_value["west_east"] = float(data[3])
            new_value["up_down"] = float(data[4])
            WindData.objects.create(**new_value)
        except ValueError:
            RawInputError.objects.create(type=RawInputError.E_INVALID, raw_input=input_data)
        except RecursionError:
            RawInputError.objects.create(type=RawInputError.E_INVALID, raw_input=input_data)


