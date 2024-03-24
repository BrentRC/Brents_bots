import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.zeros)
    def Get_Value(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        # if i == c.zeros - 1:
        #     print(self.values)
    def Save_Values(self):
        np.save('data/sensorVal.npy', self.values)