from simulation import SIMULATION
simulation = SIMULATION
# import math
# import random
# import pybullet_data
# import pybullet as p
# import time
# import pyrosim.pyrosim as pyrosim
# import numpy as np
# import constants as c
#
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(c.gravity1, c.gravity2, c.gravity3)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)
#
# backLegSensorValues = np.zeros(c.zeros)
# frontLegSensorValues = np.zeros(c.zeros)
#
# backLegTargetAngles = c.backLegTargetAngles
#
# frontLegTargetAngles = c.frontLegTargetAngles
#
#
# for i in range(c.zeros):
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = b'Torso_BackLeg',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = backLegTargetAngles[i],
#         maxForce = c.maxForce)
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotId,
#         jointName=b'Torso_FrontLeg',
#         controlMode=p.POSITION_CONTROL,
#         targetPosition= frontLegTargetAngles[i],
#         maxForce=c.maxForce)
#     time.sleep(c.sleeper)
# p.disconnect()
# np.save('data/backLegTargetAngles.npy', backLegTargetAngles)
# np.save('data/frontLegTargetAngles.npy', frontLegTargetAngles)
#
#
