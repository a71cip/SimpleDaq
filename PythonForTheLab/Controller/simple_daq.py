import time
import serial

class SimpleDaq():

    DEFAULTS = {'write_termination' : '\n',
                'read_termination' : '\n',
                'encoding' : 'ascii',
                'baudrate' : 9600,
                'write_timeout' : 1,
                'read_timeout': 1,
                }
    rsc = None

    def __init__(self,port):
        self.port=port

    def status(self):
        return self.rsc.is_open

    def initialize(self):
        self.rsc = serial.Serial(port=self.port,baudrate=self.DEFAULTS['baudrate'],timeout=self.DEFAULTS['read_timeout'],write_timeout=self.DEFAULTS['write_timeout'])
        print('Opening serial communication @ %s ...' % (self.port))
        time.sleep(3)
        #status = self.rsc.is_open  # check if the port is really open
        #if (self.status()):
        #    print('Device is open')

    def write(self, message):
        msg=(message + self.DEFAULTS['write_termination']).encode(self.DEFAULTS['encoding'])
        self.rsc.write(msg)

    def read(self):

        line = "".encode(self.DEFAULTS['encoding'])
        read_termination = self.DEFAULTS['read_termination'].encode(self.DEFAULTS['encoding'])

        while True:
            new_char = self.rsc.read(size=1)
            line += new_char
            if new_char == read_termination:
                break

        return line.decode(self.DEFAULTS['encoding'])

    def query(self, message):
        self.write(message)
        time.sleep(0.5)
        return self.read()


    def get_analog_value(self, channel):
        write_string = 'IN:CH'+str(channel)
        val = int(self.query(write_string))
        return val

    def set_digital_value(self, channel, value):
        write_string = 'DI:' + 'CH' + str(channel) + ':' + str(value)
        self.write(write_string)

    def finalize(self):
        if self.rsc is not None:
            self.rsc.close()

    def set_pwm(self, channel, value):
        pass




if __name__ == "__main__":
	dev = SimpleDaq('/dev/ttyUSB0')
	dev.initialize()	
	print(dev.query('IDN'))
	sig=dev.get_analog_value(7)
	print('ADC CH7 ANALOG : %.2f [V]' % (5*sig/1024))
	dev.finalize()
	print("Device is %s" %(dev.status()))



"""
dev = SimpleDaq('/dev/ttyUSB0')
dev.initialize()
print(dev.query('IDN'))
sig=dev.get_analog_value(7)
print('ADC CH7 ANALOG : %.2f [V]' % (sig))
dev.finalize()
print("Device is %s" %(dev.status()))
"""
