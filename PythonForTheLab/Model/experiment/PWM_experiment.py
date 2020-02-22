"""
Experiment Model
================
Building a model for the experiment allows developers to have a clear picture of the logic of their
experiments. It allows to build simple GUIs around them and to easily share the code with other users.
"""

import yaml
import os


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

if __name__ == "__main__":
    e = Experiment()
    e.load_config('experiment.yml')
    #e.load_daq()
