import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

#set up figure, axis, plot element, and text to animate
fig = plt.figure()
ax = plt.axes(xlim=(0,1), ylim=(0,1))
line, = ax.plot([], [], lw=2)
txt = ax.text(.9, .1, "", transform = ax.transAxes, ha="left")

#Defaults
# x0 = .5
# ri = 2
# rf = 4
# stepsize = .01

#Get user values
x0 = float(input("x0: "))
print("\nFor a static graph, enter the same value for initial and final r.")
ri = float(input("Initial r: "))
rf = float(input("Final r: "))

time = 5 #animation time in seconds
fps = 30

#Calculate total number of frames
frames = fps*time

#Calculate interval between frames, in ms
interval = int(time*1000 / frames)

#Calculate step size for r
stepsize = (rf - ri) / frames


#this is what is drawn for a new, clear frame
def init():
    line.set_data([], [])

    txt.set_text("")

    return line, txt

#animation  function, called sequentially by FuncAnimation
def animate(i):

    #Calculate r value for this iteration
    r = i*stepsize + ri

    #Print the current r value
    txt.set_text("r: %1.2f" % r)

    #Generate array of X-axis values
    x = np.linspace(0,1,500)

    #Calculate list of Y values
    y = [x0]
    #This list comprehension has a condensed version of
    # x_(n+1) = r*x_n(1-x_n)
    [ y.append((r*y[n-1]*(1-y[n-1]))) for n in range(len(x)-1)]

    line.set_data(x,y)
    return line, txt

#call animator. blit only redraws changed elements
#this is also a great example of python being a functional programming language!
anim = animation.FuncAnimation(fig, animate, init_func=init,
    frames=frames, interval=interval, blit=True)


#save the animation as mp4
#Requires avconv
#forces x264 to support HTML5 embedding.

#UNCOMMENT THESE LINES FOR .MP4 ENCODING
#mywriter = animation.AVConvWriter(fps=30)
#anim.save('population_animation.mp4', writer=mywriter,extra_args=['-vcodev', 'libx264', '-verbose-debug'])
#print("Done rendering animation!")


plt.show()
