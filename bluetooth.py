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

    def word_to_command(self, word):
        if word == "forward": return self.forward
        if word == "backward": return self.backward
        if word == "right": return self.right
        if word == "left": return self.left
        if word == "stop": return self.stop
        if word == "spin": return self.spin

