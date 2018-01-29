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


def BEM(h, y, lower, upper):
    interval = np.arange(lower + h, upper + h, h)
    ndsolve = np.array([y])
    for x in interval:
        # y1 = y0 + h * f(x1, y1)
        #    = y0 + h * ( 2 * x1 + y1 )
        # y1 = ( y0 + 2 * h * x1 )/( 1 - h )
        y = (y + 2 * h * x)/(1 - h)
        ndsolve = np.append(ndsolve, y)
    ndsolve = np.delete(ndsolve, -1)
    interval = np.arange(lower, upper, h)
    return interval, ndsolve

interval0, ndsolve0 = BEM(h0, y0, lower0, upper0)
l, = plt.plot(interval0, ndsolve0, 'rx')
plt.plot(np.arange(0, 1, 0.001), analytic(np.arange(0, 1, 0.001)), '--')

axcolor = 'lightgoldenrodyellow'
axh = plt.axes([0.25, 0.1, 0.5, 0.1], facecolor=axcolor)
sh = Slider(axh, 'h', 0.001, 1., valinit=0.2)


def update(val):
    h0 = sh.val
    interval0, ndsolve0 = BEM(h0, y0, lower0, upper0)
    l.set_data(interval0, ndsolve0)
    fig.canvas.draw_idle()

sh.on_changed(update)
plt.show()
