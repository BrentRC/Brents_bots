import matplotlib.pyplot as plt
import numpy
backLegSensorValues = numpy.load('data/BackLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/FrontLegSensorValues.npy')
print(backLegSensorValues)
print(frontLegSensorValues)
plt.plot(backLegSensorValues, label="BackLeg", linewidth=4)
plt.plot(frontLegSensorValues, label="FrontLeg")
plt.legend()
plt.show()
