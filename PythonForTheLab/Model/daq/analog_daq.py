"""
Analog DAQ
========
Class for communicating to a real device. Is implements the base for communicating with the device
through a Controller. The experiment in mind is measuring the I-V curve of a diode, addinge the logic
into a separate Model for the experiment may seem redundant, but incredibly useful in bigger projects.

"""

#from PythonForTheLab.Controller.simple_daq import SimpleDaq
#from PythonForTheLab.Model.daq.base import DAQBase

from ... import Q_
from ...Controller import SimpleDaq 
from .base import DAQBase



class AnalogDaq(DAQBase):
	
	def __init__(self, port):
		super().__init__()
		self.port = port
		self._driver = SimpleDaq(self.port)

	def initialize(self):
		self._driver.initialize()

	def idn(self):
		return self._driver.query('IDN')

	def get_analog_value(self, channel):
		query_string = 'IN:CH'+str(channel)
		value_int = int(self._driver.query(query_string))
		#value_volts = value_int/1024*Q_('3.3V')
		value_volts = value_int*5/1024
		return value_volts

	def set_analog_value(self, channel, value):
		pass

	def get_digital_value(self, port):
		pass

	def set_digital_value(self, port, value):
		write_string = 'DI:' + 'CH' + str(port) + ':' + str(value)
		#print(write_string)
		self._driver.write(write_string)

	








