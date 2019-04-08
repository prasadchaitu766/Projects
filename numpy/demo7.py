import numpy as np
import matplotlib.pyplot as plt


# x = np.linspace(2,5)
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# plt.plot(x,y1,x,y2)
# plt.show()


# plt.plot([10, 20, 30, 40, 50])
# plt.xlabel('X Members')
# plt.ylabel('Y Members')
# plt.show()
# plt.plot([40,50,60,43,21])
# plt.xlabel('X Members')
# plt.ylabel('y Members')
# plt.show( )
# plt.plot([3, 2, 6, 4], [6, 4, 2, 12],[2,3,4,5])
# plt.xlabel('X Members')
# plt.ylabel('Y Members')
# plt.show()
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16],'ro')
# plt.axis([0, 6, 0,60])
# plt.xlabel('X Members')
# plt.ylabel('Y Members')
# plt.show()



# t = np.arange(1, 4, 0.5)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()



# t = np.arange(1, 20,1)
# plt.plot(t, t**2, 'y-')
# plt.show()

population_age = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(population_age, bins, histtype='bar', rwidth=0.8)
plt.xlabel('age groups')
plt.ylabel('Number of people')
plt.title('Histogram')
plt.show()