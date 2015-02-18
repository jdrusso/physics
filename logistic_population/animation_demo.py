#Animation demo taken from
#https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

#set up figure, axis, and plot element to animate
fig = plt.figure()
ax = plt.axes(xlim=(0,2), ylim=(-2,2))
line, = ax.plot([], [], lw=2)

#plot background of frames
def init():
    line.set_data([], [])
    return line,

#animation  function. This is called sequentially
def animate(i):
    x = np.linspace(0,2,1000)
    y = (1-(.01*i))*np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x,y)
    return line,

#call animator. blit only redraws changed elements
#great example of functional programming language!
anim = animation.FuncAnimation(fig, animate, init_func=init,
    frames=200, interval=25, blit=True)

#save the animation as mp4
#Requires avconv
#forces x264 to support HTML5 embedding.
mywriter = animation.AVConvWriter(fps=60)
anim.save('basicanimation.mp4', writer=mywriter,extra_args=['-vcodev', 'libx264', '-verbose-debug'])

plt.show()
