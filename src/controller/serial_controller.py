import serial as pyserial


DEFAULT_SERIAL_PORT = ''
BAUD_RATE = 9600
RESPONSE_CODE_GOOD = 12


class SerialController(object):

    def __init__(self, port):
        if port is None:
            port = DEFAULT_SERIAL_PORT
        self.serial = pyserial.Serial(port, BAUD_RATE, timeout=1.0)

    def write_command(self, button, value):
        """Convert command to bytes and write to controller"""
        bytes_to_send = bytes([int(button), int(value)])
        # print('Sending: {}'.format(bytes_to_send))
        self.serial.write(bytes_to_send)
        response = int.from_bytes(self.serial.read(1), byteorder='big', signed=False)
        return response == RESPONSE_CODE_GOOD, response
