import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p
import numpy as np
class MOTOR:
    def __init__(self, jointName, robotId):
        self.jointName = jointName
        self.robotId = robotId
        self.Prepare_To_Act()
        self.motorValues = self.targetAngles
    def Prepare_To_Act(self):
        if self.jointName == b'Torso_FrontLeg':
            self.amplitude = c.amplitude
            self.frequency = c.frequency / 2
            self.offset = c.offset
        if self.jointName == b'Torso_BackLeg':
            self.amplitude = c.amplitude
            self.frequency = c.frequency
            self.offset = c.offset

        self.targetAngles = self.amplitude * np.sin(
            2 * np.pi * self.frequency * np.linspace(0, 1, c.zeros) + self.offset)

    def Set_Value(self, robotId, i):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=self.robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[i],
            maxForce=c.maxForce)

    def Save_Values(self):
        np.save('data/motorValues.npy', self.motorValues)