import serial

# Set the Bluetooth serial port name (check your operating system's Bluetooth settings)
bluetooth_port = 'COM3'  # Replace with the appropriate port for your system

# Set the baud rate (the same as configured in Arduino)
baud_rate = 9600

# Initialize the serial connection
bluetooth = serial.Serial(
    port=bluetooth_port,
    baudrate=baud_rate,
    bytesize=serial.SEVENBITS,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE
)

# Open the Bluetooth connection

# Check if the connection is successful
if bluetooth.is_open:
    print('Bluetooth connection established.')
else:
    bluetooth.open()
    print('Failed to establish Bluetooth connection.')

print(bluetooth)
# Send data to Arduino
data_to_send = 'F'
bluetooth.write(data_to_send.encode())

# Close the Bluetooth connection
bluetooth.close()