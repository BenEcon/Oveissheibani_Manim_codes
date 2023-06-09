#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation
#
## Image size (pixels)
#width = 600
#height = 600
#
## Plotting window
#xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
#
## Maximum number of iterations
#max_iter = 50
#
#def mandelbrot(c):
#    z = c
#    for n in range(max_iter):
#        if abs(z) > 2:
#            return n
#        z = z*z + c
#    return max_iter
#
#def draw_mandelbrot(xmin, xmax, ymin, ymax, ax):
#    # Generate a 2D array to store the image data
#    img = np.empty((width, height))
#    for i, x in enumerate(np.linspace(xmin, xmax, width)):
#        for j, y in enumerate(np.linspace(ymin, ymax, height)):
#            img[i, j] = mandelbrot(x + 1j*y)
#
#    ax.imshow(img, extent=(xmin, xmax, ymin, ymax), cmap='hot', animated=True)
#
#fig, ax = plt.subplots()
#
#def animate(i):
#    ax.clear()
#    zoom = 0.05 * i
#    draw_mandelbrot(xmin + zoom, xmax - zoom, ymin + zoom, ymax - zoom, ax)
#
#ani = FuncAnimation(fig, animate, frames=20)
#
#ani.save('mandelbrot_zoom.mp4', fps=15)
#
#plt.show()



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

# Adjust these values as desired
zoom_center_x = 1.0
zoom_center_y = 1.0

def animate(i):
    ax.clear()
    ax.set_axis_off()
    
    x, y = np.meshgrid(np.linspace(-2.0, 1.0, 800), np.linspace(-1.5, 1.5, 800))
    c = x + 1j * y
    mandelbrot_set = np.zeros(c.shape, float)
    for n in range(50):
        z = mandelbrot_set**3 + c
        mandelbrot_set[z > 1000] = 2
        z[z > 1000] = 2
    mandelbrot_set[abs(z) < 1000] = 0

    ax.imshow(np.log(mandelbrot_set), extent=[-2.0, 1.0, -1.5, 1.5])
    
    # adjust the xlim and ylim to zoom into the desired center
    ax.set_xlim([zoom_center_x - 1 + i * 0.03, zoom_center_x + 1 - i * 0.02])
    ax.set_ylim([zoom_center_y - 1 + i * 0.02, zoom_center_y + 1 - i * 0.02])

ani = FuncAnimation(fig, animate, frames=np.arange(0, 200, 0.1), interval=100)

# Save the animation
ani.save('mandelbrot_zoom.mp4', writer='ffmpeg')

plt.show()
