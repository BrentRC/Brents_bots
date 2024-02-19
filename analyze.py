import matplotlib.pyplot as plt
import numpy
# backLegSensorValues = numpy.load('data/BackLegSensorValues.npy')
# frontLegSensorValues = numpy.load('data/FrontLegSensorValues.npy')
# print(backLegSensorValues)
# print(frontLegSensorValues)
# plt.plot(backLegSensorValues, label="BackLeg", linewidth=4)
# plt.plot(frontLegSensorValues, label="FrontLeg")
sin_vec = numpy.load('data/sin_vecValues.npy')
print(sin_vec)
plt.plot(sin_vec, label="sin_vec")
plt.legend()
plt.show()
