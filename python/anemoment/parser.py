class Parser:
    """
    Parses input from an Anemoment TriSonica.
    """

    def __init__(self, serial):
        """
        :param serial: The open serial connection to parse
        :type serial: serial.Serial
        """
        self.__serial = serial
        if not self.__serial.is_open:
            self.__serial.open()




