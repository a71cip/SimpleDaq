import numpy as np
import pint
import time
from .analog_daq import AnalogDaq

#dev = AnalogDaq('/dev/TTYUSB0')
#dev.idn()
#print("This is the init of the daq")

ur = pint.UnitRegistry()
V = ur('V')

daq = AnalogDaq('/dev/ttyUSB0')
daq.initialize()

print('Serial Number : %s' %(daq.idn()))

adc = daq.get_analog_value(0)*V
print('Voltage at AD0 : %s' %(adc))

daq.set_digital_value(13,1)
time.sleep(1)

daq.set_digital_value(13,0)
time.sleep(1)





