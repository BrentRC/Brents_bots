import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p
import numpy as np
class MOTOR:
    def __init__(self, jointName, robotId):
        self.jointName = jointName.decode('utf-8')
        self.robotId = robotId

    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=self.robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.maxForce)
