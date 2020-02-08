"""
Plotting a png image
"""
import plotting
from image import file2image

img = file2image('img01.png')

img_plot = []
for y, _ in enumerate(img[::-1]):
    line = [complex(x, y) for x, rgb in enumerate(img[y][::-1]) if rgb[0] < 120]
    for dot in line:
        img_plot.append(dot)

plotting.plot(img_plot[::-1], 200)

input('press any key to continue')
