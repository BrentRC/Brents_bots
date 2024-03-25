import copy
from solution import SOLUTION
import constants as c
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for x in range(c.populationSize):
            self.parents[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1


    def Evolve(self):
        # self.parent.Evaluate("DIRECT")
        # for currentGeneration in range(c.numberOfGenerations):
        #     if currentGeneration == 0:
        #         self.parent.Evaluate("GUI")
        #     self.Evolve_For_One_Generation()
        for key in self.parents:
            self.parents[key].Start_Simulation("GUI")
        for key in self.parents:
            self.parents[key].Wait_For_Simulation_To_End()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Print(self):
        print("\nParent fitness:", self.parent.fitness, ", Child fitness:", self.child.fitness)

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child

    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        pass
