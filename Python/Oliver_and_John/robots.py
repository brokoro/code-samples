import matplotlib.pyplot as plt
import code
from math import cos, sin, pi

fig = plt.figure()
pos = [0,0]
orientation = 0
line, = plt.plot([],[], markersize=20)
plt.xlim([-10,10])
plt.ylim([-10,10])

def go(dist):
    global pos
    pos[0] += dist*cos(orientation*pi/180)
    pos[1] += dist*sin(orientation*pi/180)
    update_disp()

def spin(ang):
    global orientation
    orientation += ang
    update_disp()

def update_disp():
    line.set_marker((3,0,orientation-90))
    line.set_data(*pos)
    fig.canvas.draw()

update_disp()
plt.show(block=False)

ic = code.InteractiveConsole(locals=locals())
ic.interact()