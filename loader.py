
import MySQLdb
import serial
import datetime

from threading import Thread


class Parser:
    """
    Parses input from an Anemoment TriSonica.
    """

    def __init__(self):
        """
        :param serial: A serial connection to continuously parse
        :type serial: serial.Serial
        """
        UART = "/dev/ttyAMA0"
        if UART is not None:
            ser = serial.Serial(port=UART, baudrate=115200)
        else:
            ser = None

        self.__serial = ser
        self.db = MySQLdb.connect(host="localhost",  # your host
                             user="anemomentuser",  # username
                             passwd="mix case fire aloud",  # password
                             db="anemoment")  # name of the database


    def add_wind_data(self, **kwargs):
        cur = self.db.cursor()
        cur.execute("""INSERT INTO anemoment_winddata (speed, direction, north_south, west_east, up_down, temperature, timestamp)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
                       (
                           kwargs['speed'], 
                           kwargs['direction'], 
                           kwargs['north_south'], 
                           kwargs['west_east'],
                           kwargs['up_down'],
                           kwargs['temperature'],
                           datetime.datetime.now()
                       )
                       )
        self.db.commit()


    def worker(self):
        # remove the b' ...\r\n'
        while 1:
            self.parse_string(str(self.__serial.readline())[3:-4])

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
            # RawInputError.objects.create(type=RawInputError.E_INCOMPLETE, raw_input=input_data)
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
            # WindData.objects.create(**new_value)
            self.add_wind_data(**new_value)
        except ValueError:
            # RawInputError.objects.create(type=RawInputError.E_INVALID, raw_input=input_data)
            print("valueerror")
        except RecursionError:
            # RawInputError.objects.create(type=RawInputError.E_INVALID, raw_input=input_data)
            pass


p = Parser()
p.worker()


