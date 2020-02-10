"""
Plotting a png image
"""
import plotting
from image import file2image

img = file2image('img01.png')

img_plot = []
for y, _ in enumerate(img):
    line = [complex(x, y) for x, rgb in enumerate(img[y]) if rgb[0] < 120]
    for dot in line:
        img_plot.append(dot)




if __name__ == '__main__':
    from task_1_4_11 import rotate
    plotting.plot(rotate(img_plot), 200)

    input('press any key to continue')
