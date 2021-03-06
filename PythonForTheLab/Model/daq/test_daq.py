import numpy as np
import pint
import time
from .analog_daq_NANO import AnalogDaq

#dev = AnalogDaq('/dev/TTYUSB0')
#dev.idn()
#print("This is the init of the daq")

ur = pint.UnitRegistry()
V = ur('V')

daq = AnalogDaq('/dev/ttyUSB0')
daq.initialize()

if (daq.status()):
	print("Device is open")

print('Serial Number : %s' %(daq.idn()))

adc = daq.get_analog_value(0)*V
print('Voltage at AD0 : %s' %(adc))

daq.set_digital_value('05',1)
time.sleep(1)

daq.set_digital_value('05',0)
time.sleep(0.5)

daq.pwm('05',255)
time.sleep(0.5)

daq.pwm('05',128)
time.sleep(0.5)

daq.pwm('05',0)
time.sleep(0.5)

daq.finalize()

if (not daq.status()):
	print("Device is close")







