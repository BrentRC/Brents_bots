from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import time
import constants as c
class SIMULATION:
    def __init__(self, directOrGui):
        if directOrGui == "DIRECT":
            physicsClient = p.connect(p.DIRECT)
        else:
            pysicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.gravity1, c.gravity2, c.gravity3)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(c.zeros):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            time.sleep(c.sleeper)
    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()
