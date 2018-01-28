import numpy as np
import matplotlib.pyplot as plt

# dy/dx = 2x + y ; y(0) = 1 , h = 0.2 , x in [ 0 , 1 ]
# analytical solution: y(x) = -( 2 * x + 1 ) + 3 * e ^ x

h = 0.2
y = 1
lower = 0
upper = 1
interval = np.arange(lower, upper + h, h)
ndsolve = np.array([y])

def analytic(x):
    return -2 * ( x + 1 ) + 3 * np.e ** x

def f(x, y):
    return 2 * x + y

for x in interval:
    y = y + h * f(x, y)
    ndsolve = np.append(ndsolve,y)

ndsolve = np.delete(ndsolve, -1)
plt.plot(interval,ndsolve,'rx')
plt.plot(np.arange(0,1,0.001),analytic(np.arange(0,1,0.001)),'--')
plt.show()
