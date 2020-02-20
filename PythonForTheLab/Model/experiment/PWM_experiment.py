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
            ee = yaml.load(f)

        print (ee['Experiment'])
        for k in ee['Experiment']:
            print(k)
            print(ee['Experiment'][k])
            print(10*'-')


if __name__ == "__main__":
    e = Experiment()
    e.load_config('experiment.yml')
    #e.load_daq()
