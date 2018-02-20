import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# dy/dx = 2x + y ; y(0) = 1 , h = 0.2 , x in [ 0 , 1 ]
# analytical solution: y(x) = -( 2 * x + 1 ) + 3 * e ^ x

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

h0 = 0.2
y0 = 1
lower0 = 0
upper0 = 1


def analytic(x):
    return -2 * (x + 1) + 3 * np.e ** x


def f(x, y):
    return 2 * x + y


def RKM_2(h, y, lower, upper):
    interval = np.arange(lower + h, upper + h, h)
    ndsolve = np.array([y])
    for x in interval:
        # k1 = h * f(x0, y0)
        # k2 = h * f(x0 + h, y0 + k1)
        # y1 = y0 + (h/2) * (k1 + k2)
        #    = y0 + (h/2) * (f(x0, y0) + f(x0 + h, y0 + k1))
        #    = y0 + (h/2) * (2 * x0 + y0 + 2 * (x0 + h) + y0 + h * (2 * x0 + y0))
        y = y + (h/2) * (2 * x + y + 2 * (x + h) + y + h * (2 * x + y))
        ndsolve = np.append(ndsolve, y)
    ndsolve = np.delete(ndsolve, -1)
    interval = np.arange(lower, upper, h)
    return interval, ndsolve

interval0, ndsolve0 = RKM_2(h0, y0, lower0, upper0)
l, = plt.plot(interval0, ndsolve0, 'rx')
plt.plot(np.arange(0, 1, 0.001), analytic(np.arange(0, 1, 0.001)), '--')

axcolor = 'lightgoldenrodyellow'
axh = plt.axes([0.25, 0.1, 0.5, 0.1], facecolor=axcolor)
sh = Slider(axh, 'h', 0.001, 1., valinit=0.2)


def update(val):
    h0 = sh.val
    interval0, ndsolve0 = RKM_2(h0, y0, lower0, upper0)
    l.set_data(interval0, ndsolve0)
    fig.canvas.draw_idle()

sh.on_changed(update)
plt.show()
