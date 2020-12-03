# Ok people, don't get too picky.  This is my first python program from scratch, so I'm sure there is a hot mess of
# stupid in here, but a lot of learning.

import numpy as np
import random

random.seed()

DEBUG = 0

# Here is a list of my shirts
# Colors
colors = ["Black/Grey", "Light Grey", "ROP", "Blue", "Green", "Other"]
ncolors = len(colors)

# Ok, listen.  I know having these on one line isn't the python way.  My syntax is pretty clean otherwise, but this
# is just too friggin simple and readable, so deal with it.
if DEBUG == 1: print(ncolors)
# Themes
themes = ["Company", "Run", "Ohack", "Fatty", "Other"]
nthemes = len(themes)
if DEBUG == 1: print(nthemes)

# Now, a visualization of the matrix
# blank		 Black/Grey  Light Grey    ROP    Blue   Green   Other
# Company
# Run
# Ohack
# Fatty
# Other

# Translate the array into actual counts of shirts per category
# Here is what I suspect, but do not know:
#  This is a hard math problem masquerading as an interesting programming problem.  Given a collection of items
#  with N (=2) dimensions, how can you sort those items so that no two dimensions are adjacent to each other
#  in the final list?  I suspect there is some interesting set theory math, or ... but it's outside of my
#  level, so here we are.

# Also, if I may, I'm sure there is a good reason, but array indices in numpy are counterintuitive for me.
# One dimensional array:  initial is on the X axis
# two dimensional array:  initial is on the Y axis and second is on the X axis
# Huh?  Maybe just thinking about it wrong.
tshirt = np.array([[0, 1, 0, 5, 4], [1, 2, 0, 0, 0], [1, 2, 3, 1, 0], [3, 0, 0, 0, 1], [0, 1, 3, 0, 0],
                   [0, 0, 0, 0, 2]])

shirts = tshirt.sum()
if DEBUG == 1: print(shirts)
shirt_list = []

# Subroutine to print arrays for me.  Probably a python builtin for this.


def print_array(label, array):
    for i in range(0, len(array) - 1):
        print(label, array[i])
    return 1

# Ok, so this where I do the initial sort of dealing with the data as a matrix and things start to get funny


def matrix_shirts(shirt_list):
    shirt = 0

    # Probably not the first hack.  Use counters to prevent infinite looping.
    max_counter = 50
    base_counter = 30
    counter = 0
    lastcolor = ncolors  # just an initial
    lasttheme = nthemes

    # I initially did this with for loops, because that made sense.  Then I learned that python for loops
    # are really for X in Y loops, and you can't do all the fun you can do with for(i=0;i<X;i++) loops, so it
    # had to be whiles, or at least not for.
    while shirt <= shirts and counter < max_counter:
        random.seed()
        color = random.randint(0, ncolors - 1)  # start in a random place to work through local maxima
        # So what does that mean?  You can imagine a matrix where you walk it every time and it can never
        # be solved if you always start from the same place.  So, let's start someplace random.
        while color < ncolors and counter < max_counter:
            theme = 0
            counter += 1
            if DEBUG == 1: print("in color", color, theme)
            while theme < nthemes and counter < max_counter:
                if DEBUG == 1: print("in theme", color, theme, shirt, counter, max_counter)
                if counter > base_counter:  # if we've iterated a lot, use random to try to avoid local maxima
                    if DEBUG == 1: print("Randomizing")
                    random.seed()
                    color = random.randint(0, ncolors - 1)
                    theme = random.randint(0, nthemes - 1)
                if tshirt[color, theme] > 0 and color != lastcolor and theme != lasttheme:
                    counter += 1
                    # Move this to putting in an array so we can try to slot other shirts in at the end
                    if DEBUG == 1: print("Success:", colors[color], themes[theme], shirt)
                    shirt_list.append([colors[color], themes[theme]])
                    tshirt[color, theme] -= 1
                    lastcolor = color
                    lasttheme = theme
                    shirt += 1
                    # Now we don't want the next to be same theme or color, so increment both
                    # I think this is sort of clever, without being a sort.  In a matrix, if I increment both
                    # x and y, there is no way for it to be adjacent.
                    theme += 1
                    color += 1
                else:
                    theme += 1
                if theme > nthemes:  # check to see if we marched it off the end, so let's wrap it
                    theme = 0
        color += 1
        if color >= ncolors:
            color = 0
        if DEBUG == 1: print("color increment", color)
    return shirts - shirt

# Ok, so now we have an array of shirts that are sorted, and all the crap in tshirt.numpy that we want to put into
# an array to allow us to iterate


def array_shirts(shirt_array):
    remaining_shirts = []

    # build an array of the remaining shirts
    for color in range(0, ncolors):
        for theme in range(0, nthemes):
            if tshirt[color, theme] > 0:
                for f in range(0, tshirt[color, theme]):  # there could be a bunch of them
                    remaining_shirts.append([colors[color], themes[theme]])

    # Print that remaining array out
    if DEBUG == 1: print_array("remaining", remaining_shirts)

    # Look at what we already have
    if DEBUG == 1: print("length", len(shirt_array))
    if DEBUG == 1: print_array("existing", shirt_array)

    if DEBUG == 1: print("Starting the sorting")

    # Need to make sure we know before and after of our shirts
    last_color = "undef"
    last_theme = "undef"
    existing = 0
    # It would be more efficient to swap existing and remaining in most cases, but I wrote it this way, so...
    while existing < len(shirt_array):
        color = shirt_array[existing][0]
        theme = shirt_array[existing][1]
        if DEBUG == 1: print("Existing", color, theme)
        # first time through we can just insert.  after that, need to be smarter
        for remaining in range(0, len(remaining_shirts) - 1):
            remaining_color = remaining_shirts[remaining][0]
            remaining_theme = remaining_shirts[remaining][1]
            if DEBUG == 1: print("\tRemaining", remaining_color, remaining_theme, "versus", color, theme)
            if remaining_color != color and remaining_theme != theme:
                if DEBUG == 1: print("\t\tinserting these", remaining_color, remaining_theme, "in front of ", color,
                                     theme, "and last is ", last_color, last_theme)
                shirt_array.insert(existing, [remaining_color, remaining_theme])
                remaining_shirts.remove([remaining_color, remaining_theme])
                existing += 1
                break
            else:
                existing += 1
        last_color = color
        last_theme = theme
        existing += 1

    print("Final List:")
    print_array("Final", shirt_array)

    return 1


# Press the green button in the gutter to run the script, because this is what pycharms tells you.  :P
# doesn't work for me because I haven't bothered to figure out how to get numpy into venv
if __name__ == '__main__':

    # do the matrix analysis of the shirts
    matrix_return = matrix_shirts(shirt_list)
    # if there are shirts left (hint, there probably will be)
    if matrix_return > 0:
        if DEBUG == 1: print("Had shirts remaining", matrix_return)
        array_shirts(shirt_list)  # then array sort them
    else:
        if DEBUG == 1: print("Guess we got them all", matrix_returns)
