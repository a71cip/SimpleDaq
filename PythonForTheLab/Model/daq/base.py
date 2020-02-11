"""
Base DAQ
========
Base class for the DAQ objects. It keeps track of the functions that every new model should implement.
This helps keeping the code organized and to mantain downstream compliancy

"""

class DAQBase(object):
	
	def __init__(self):
		pass

	def idn(self):
		pass

	def get_analog_value(self, channel):
		pass

	def set_analog_value(self, channel, value):
		pass

	def get_digital_value(self, port):
		pass

	def set_digital_value(self, port, value):
		pass

	


