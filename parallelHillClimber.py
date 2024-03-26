import copy
from solution import SOLUTION
import constants as c
import os
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        for x in range(c.populationSize):
            self.parents[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1


    def Evolve(self):
        # self.parent.Evaluate("DIRECT")
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.children = {}
        for key in self.parents:
            self.Spawn(key)
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Print(self):
        for key in self.parents:
            print("")
            print(f"Parent fitness for key {key}: {self.parents[key].fitness}, Child fitness for key {key}: {self.children[key].fitness}")
            print("")
    def Spawn(self, key):
        self.children[key] = copy.deepcopy(self.parents[key])
        self.children[key].Set_ID(self.nextAvailableID)
        self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):
        for key in self.parents:
            if self.children[key].fitness < self.parents[key].fitness:
                self.parents[key] = self.children[key]

    def Show_Best(self):
        best = min(self.parents, key=lambda key: self.parents[key].fitness)
        self.parents[best].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for key in solutions:
            solutions[key].Start_Simulation("DIRECT")
        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()