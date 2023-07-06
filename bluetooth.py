import serial

class Arduino:
    forward = "F"
    backward = "B"
    right = "R"
    left = "L"
    stop = "S"
    spin = "Q"
    
    def __init__(self, com, baud_rate):
        self.com = com
        self.baud_rate = baud_rate
        self.bluetooth = serial.Serial(
            port=self.com,
            baudrate=self.baud_rate
            ,
            bytesize=serial.SEVENBITS,
            parity=serial.PARITY_EVEN,
            stopbits=serial.STOPBITS_ONE
        )
    def send_command(self, command):
        self.bluetooth.write(command.encode())

