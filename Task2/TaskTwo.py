
import heartpy as hp
import matplotlib.pyplot as plt

sample_rate = 10000

data = hp.get_data('normal__201102260502_Output_mono.csv')
plt.plot(data)
plt.show()
readData, measurements = hp.process(data, sample_rate)

hp.plotter(readData, measurements)
for measure in measurements.keys():
    print('%s: %f' %(measure, measurements[measure]))




