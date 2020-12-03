import numpy as np
import random

random.seed(2)

# Colors
colors = ["Black/Grey", "Light Grey", "ROP", "Blue", "Green", "Other"]
# Themes
themes = ["Company", "Run", "Ohack", "Fatty", "Other"]

# blank		 Black/Grey  Light Grey    ROP    Blue   Green   Other
# Company
# Run
# Ohack
# Fatty
# Other

# tshirt = np.array([[2, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 2, 0],
#                   [0, 2, 0, 0, 2, 1, 0], [0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1]])

tshirt = np.array([[0, 1, 0, 5, 4], [1, 2, 0, 0, 0], [1, 2, 3, 1, 0], [3, 0, 0, 0, 1], [0, 1, 3, 0, 0],
                   [0, 0, 0, 0, 2]])


ncolors = len(colors)
print(ncolors)
nthemes = len(themes)
print(nthemes)
shirts = tshirt.sum()
print(shirts)
lastcolor = ncolors   # just an initial
lasttheme = nthemes

shirt = 0
max_counter = 100
counter = 0

while shirt <= shirts and counter < max_counter:
    random.seed()
    color = random.randint(0, ncolors - 1)
    while color < ncolors and counter < max_counter:
        theme = 0
        counter += 1
#        print("in color", color, theme)
        while theme < nthemes and counter < max_counter:
#           print("in theme", color, theme, shirt, counter)
            if counter > (max_counter / 0.75):  # if we've iterated a lot, use random to try to avoid local maxima
                random.seed()
                color = random.randint(0, ncolors - 1)
                theme = random.randint(0, nthemes - 1)
            if tshirt[color, theme] > 0 and color != lastcolor and theme != lasttheme:
                counter += 1
                # Move this to putting in an array so we can try to slot other shirts in at the end
                print(colors[color], themes[theme], shirt)
                tshirt[color, theme] -= 1
                lastcolor = color
                lasttheme = theme
                shirt += 1
                # Now we don't want the next to be same theme or color, so increment both
                theme += 1
                color += 1
            else:
                theme += 1
            if theme > nthemes:  # check to see if we marched it off the end, so let's wrap it
                theme = 0
            if color > ncolors:
                color = 0
        color += 1

if counter >= max_counter:
    print("Failed solve.  Try again.", shirt)
