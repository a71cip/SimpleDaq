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
        path = os.path.join(os.path.expanduser('~'),'PyCharmProjects','OpenCV-Lab','SimpleDaq','PythonForTheLab','Model','experiment','PWM_experiment.py')
        print(path)



if __name__ == "__main__":
    e = Experiment()
    e.load_config('..../Example/Config/experiment.yml')
    #e.load_daq()
