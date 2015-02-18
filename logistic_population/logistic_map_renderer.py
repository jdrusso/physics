#Animation demo taken from
#https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

#set up figure, axis, and plot element to animate
fig = plt.figure()
ax = plt.axes(xlim=(0,1), ylim=(-2,2))
line, = ax.plot([], [], lw=2)

txt = fig.text(.2, .2, "")

#Initial populaton size
x0 = .5
r0 = 2

x0 = float(input("x0: "))
r0 = float(input("r0: "))


#plot background of frames
def init():
    line.set_data([], [])

    return line,

#animation  function. This is called sequentially
def animate(i):

    r = i*.01 + r0

    txt.set_text("r: %1.2f" % r)

    x = np.linspace(0,1,500)

    #Calculate list of Y values
    y = [x0]
    [ y.append((r*y[n-1]*(1-y[n-1]))) for n in range(len(x)-1)]

    line.set_data(x,y)
    return line,

#call animator. blit only redraws changed elements
#great example of functional programming language!
anim = animation.FuncAnimation(fig, animate, init_func=init,
    frames=200, interval=10, blit=False)

#save the animation as mp4
#Requires avconv
#forces x264 to support HTML5 embedding.
mywriter = animation.AVConvWriter(fps=40)
#anim.save('basicanimation.mp4', writer=mywriter,extra_args=['-vcodev', 'libx264', '-verbose-debug'])

print("Done rendering animation!")

#TODO: embed this in an ipython notebook

plt.show()
