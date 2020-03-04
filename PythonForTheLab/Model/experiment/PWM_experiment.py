"""
Experiment Model
================
Building a model for the experiment allows developers to have a clear picture of the logic of their
experiments. It allows to build simple GUIs around them and to easily share the code with other users.
"""

import yaml
import os
import time
import numpy as np


class Experiment:
    """Class for performing a pwm sequence
    """

    def __init__(self):
        self.daq = None
        self.properties = {}


    def load_config(self, filename=None):
        os.chdir("/home/cip/PycharmProjects/OpenCV-Lab/SimpleDaq/Examples/Config")

        with open(filename, 'r') as f:
            #ee = yaml.load(f)
            params = yaml.load(f, Loader=yaml.FullLoader)

        #print (ee['Experiment'])
        #for k in ee['Experiment']:
        #    print(k)
        #    print(ee['Experiment'][k])
        #    print(10*'-')

        self.properties = params
        #print(self.properties)
        self.properties['config_file'] = filename
        user  = self.properties['User']['name']
        role  = self.properties['User']['role']
        type  = self.properties['User']['type']
        daq   = self.properties['DAQ']['name']
        port  = self.properties['DAQ']['port']
        ch    = self.properties['Sequence']['channel']
        step  = self.properties['Sequence']['step']
        delay = self.properties['Sequence']['delay']


        print('Experiment file : %s' %(self.properties['config_file']))
        print('User : %s' %(user))
        print('Role : %s' %(role))
        print('Experiment type : %s' %(type))
        print('Daq : %s' %(daq))
        print('Port : %s' %(port))
        print('Pwm channel : %s' %(ch))
        print('Pwm step : %s' %(step))
        print('Pwm delay : %s' %(delay))


    def load_daq(self, daq_model=None):
        """ Loads a DAQ Model already initialized or loads from yaml specifications. The DAQ that can
        be provided through the YAML are 'DummyDaq' and 'RealDaq'. There are no limitations regarding
        an already initialized DAQ provided that follows the Daq Model.
        :param daq_model: it can be a model already initailized. If not provided, loads the default.
        """

        if daq_model is None:
            if 'DAQ' in self.properties:
                name = self.properties['DAQ']['name']
                port = self.properties['DAQ']['port']

                if name == 'DummyDaq':
                    #from PythonForTheLab.Model.daq import DummyDaq
                    #self.daq = DummyDaq(port)
                    pass

                elif name == 'Nano':
                    print('NANO')
                    from ..daq.analog_daq_NANO import AnalogDaq
                    self.daq = AnalogDaq(port)
                    self.daq.initialize()

                    if (self.daq.status()):
                        print("Device is open")

                    print('Serial Number : %s' % (self.daq.idn()))

                    adc = self.daq.get_analog_value(0)
                    print('Voltage at AD0 : %s' % (adc))

                    self.daq.set_digital_value('05', 1)
                    time.sleep(1)

                    self.daq.set_digital_value('05', 0)
                    time.sleep(0.5)
                    """
                    self.daq.pwm('05', 255)
                    time.sleep(0.5)

                    self.daq.pwm('05', 128)
                    time.sleep(0.5)

                    self.daq.pwm('05', 0)
                    time.sleep(0.5)
                    """
                    #self.daq.finalize()

                    #if (not self.daq.status()):
                    #    print("Device is close")

                elif name == 'PyVisa':
                    #from PythonForTheLab.Model.daq.visa_daq import AnalogDaq
                    #self.daq = AnalogDaq(port)
                    pass
                else:
                    filename = self.properties['config_file']
                    raise Exception('The daq specified in {} does not exist in this program'.format(filename))
            else:
                filename = self.properties['config_file']
                raise Exception("No DAQ specified in {}".format(filename))
        else:
            self.daq = daq_model

    def do_pwm(self):
        ch = self.properties['Sequence']['channel']
        start = self.properties['Sequence']['start']
        stop = self.properties['Sequence']['stop']
        step = self.properties['Sequence']['step']
        delay = self.properties['Sequence']['delay']
        print(ch)
        print(step)
        print(delay)


        pwm_values = np.linspace(start, stop, step)
        print(pwm_values)


        for value in pwm_values:
            pwm_now = value
            #self.daq.pwm('05', pwm_now)
            #time.sleep(10)
            #print(pwm_now)
            self.daq.pwm(ch, pwm_now)
            time.sleep(delay/1000)

        time.sleep(0.5)
        self.daq.pwm(ch, 0)
        self.daq.finalize()

        if (not self.daq.status()):
            print("Device is close")

        """
        self.daq.pwm('05', 255)
        time.sleep(0.5)

        self.daq.pwm('05', 128)
        time.sleep(0.5)

        self.daq.pwm('05', 0)
        time.sleep(0.5)
        """

#if __name__ == "__main__":
e = Experiment()
e.load_config('experiment.yml')
e.load_daq()
e.do_pwm()
