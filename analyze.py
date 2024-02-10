import matplotlib.pyplot as plt
import numpy
backLegSensorValues = numpy.load('data/back_leg_sensor_values.npy')
print(backLegSensorValues)
plt.plot(backLegSensorValues)
plt.show()
