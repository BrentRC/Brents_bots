import numpy as np
gravity1 = 0
gravity2 = 0
gravity3 = -9.8
zeros = 1000

backLegAmplitude = np.pi/2
backLegFrequency = 10
backLegPhaseOffset = 0
backLegTargetAngles = backLegAmplitude * np.sin(2 * np.pi * backLegFrequency * np.linspace(0, 1, 1000) + backLegPhaseOffset)

frontLegAmplitude = np.pi/3
frontLegFrequency = 11
frontLegPhaseOffset = 0
frontLegTargetAngles = frontLegAmplitude * np.sin(2 * np.pi * frontLegFrequency * np.linspace(0, 1, 1000) + frontLegPhaseOffset)

maxForce = 50
sleeper = 1/60